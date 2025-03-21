from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

# Flask 애플리케이션 생성
app = Flask(__name__)

# ------------------------
# 데이터베이스 설정
# ------------------------

# SQLAlchemy에서 사용할 기본 베이스 클래스 정의
class Base(DeclarativeBase):
    pass

# SQLite 데이터베이스 경로 설정 (현재 디렉토리에 cafes.db 생성)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'

# SQLAlchemy 객체 생성 (Flask와 연결)
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# ------------------------
# 데이터베이스 테이블 정의
# ------------------------

# Cafe 테이블 정의 (SQLAlchemy ORM 사용)
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # 기본 키
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # 카페 이름
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)  # 구글 지도 URL
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)  # 이미지 URL
    location: Mapped[str] = mapped_column(String(250), nullable=False)  # 위치 (도시명 등)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)  # 좌석 정보
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)  # 화장실 유무
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)  # 와이파이 유무
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)  # 콘센트 유무
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)  # 통화 가능 여부
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)  # 커피 가격

    # JSON 형태로 변환하는 헬퍼 메서드
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# 앱 실행 시 DB 테이블이 없다면 생성
with app.app_context():
    db.create_all()

# ------------------------
# 라우트 정의 (API 엔드포인트)
# ------------------------

# 기본 홈페이지 렌더링
@app.route("/")
def home():
    return render_template("index.html")

# 무작위 카페 1개 반환
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

# 모든 카페 정보를 반환
@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

# 특정 위치에 있는 카페 조회 (예: /search?loc=Seoul)
@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# 새로운 카페 추가 (POST 방식, Postman에서 테스트 가능)
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# 특정 카페의 커피 가격 업데이트 (PATCH 방식, 예: /update-price/3?new_price=₩4500)
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

# 특정 카페 삭제 (DELETE 방식, API key 필요)
# 예: /report-closed/2?api-key=TopSecretAPIKey
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

# ------------------------
# 애플리케이션 실행
# ------------------------
if __name__ == '__main__':
    app.run(debug=True)
