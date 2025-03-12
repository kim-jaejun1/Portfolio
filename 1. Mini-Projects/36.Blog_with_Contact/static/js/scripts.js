/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/

// 문서의 DOM이 완전히 로드된 후 실행
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0; // 이전 스크롤 위치 저장 변수
    const mainNav = document.getElementById('mainNav'); // 네비게이션 바 요소 가져오기
    const headerHeight = mainNav.clientHeight; // 네비게이션 바의 높이 저장

    // 스크롤 이벤트 리스너 추가
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1; // 현재 스크롤 위치 계산

        if (currentTop < scrollPos) { // 스크롤을 위로 올리는 경우
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible'); // 네비게이션 바가 고정된 상태라면 'is-visible' 클래스 추가
            } else {
                console.log(123); // 디버깅용 콘솔 출력
                mainNav.classList.remove('is-visible', 'is-fixed'); // 네비게이션 바 숨김
            }
        } else { // 스크롤을 아래로 내리는 경우
            mainNav.classList.remove('is-visible'); // 'is-visible' 클래스 제거
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed'); // 특정 높이 이상으로 스크롤되면 네비게이션 바 고정
            }
        }
        scrollPos = currentTop; // 현재 스크롤 위치 업데이트
    });
});
