import numpy as np
import matplotlib.pyplot as plt

# 시그모이드 함수 및 그 도함수
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 학습 데이터
X = np.array([[0.0], [0.1], [0.2], [0.3], [0.4], [0.5],
              [0.6], [0.7], [0.8], [0.9], [1.0]])
y = np.array([[0.00], [0.36], [0.64], [0.84], [0.96],
              [1.00], [0.96], [0.84], [0.64], [0.36], [0.00]])

# 신경망 구조
input_size = 1
hidden_size = 4
output_size = 1

# 가중치 초기화
np.random.seed(42)
weights_input_hidden = np.random.uniform(-1, 1, (input_size, hidden_size))
weights_hidden_output = np.random.uniform(-1, 1, (hidden_size, output_size))

# 학습률 및 반복 횟수
learning_rate = 0.7
iterations = 500000

# 학습 과정
for i in range(iterations):
    # 순전파
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = sigmoid(final_input)

    # 오차 계산
    error = y - final_output

    # 역전파
    d_output = error * sigmoid_derivative(final_output)  # 출력층의 gradient
    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)  # 은닉층의 gradient

    # 가중치 업데이트
    weights_hidden_output += hidden_output.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden) * learning_rate

    # 학습 상태 출력 (100000번마다)
    if i % 100000 == 0:
        loss = np.mean(np.square(error))
        print(f"Iteration {i}, Loss: {loss}")

# 결과 시각화
plt.plot(X, y, 'ro', label='Actual Data')  # 실제 데이터
plt.plot(X, final_output, 'b-', label='Predicted')  # 예측 결과
plt.xlabel('Input (x)')
plt.ylabel('Output (f(x))')
plt.legend()
plt.title('Neural Network Approximation of f(x) = 4x(1 - x)')
plt.show()
