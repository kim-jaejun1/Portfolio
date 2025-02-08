import numpy as np
import matplotlib.pyplot as plt

# Sigmoid activation function and derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR input data (4행 2열)
X = np.array([
    [1,1],
    [1,0],
    [0,1],
    [0,0]
])

# Expected output
y = np.array([[0], [1], [1], [0]])  # 4행 1열

# Adding bias to input
X_bias = np.hstack((X, np.ones((X.shape[0], 1))))
# [[1,1,1]
#  [1,0,1]
#  [0,1,1]
#  [0,0,1]]

# initial weights and bias
np.random.seed(42)
w_input_hidden = np.array([
    [0.4, -0.3],
    [-0.35, 0.45],
    [0.3, 0.3]
])

w_hidden_output = np.array([
    [0.5],
    [-0.6],
    [0.4]
])

# Learning rate
learning_rate = 0.02

# number of epochs
epochs = 100000

# To record error for plotting
errors = []

# Error Backpropagation Training loop
for epoch in range(epochs):
    # forward pass
    hidden_input = np.dot(X_bias, w_input_hidden) # 행렬 곱 = 앞 행렬의 열 개수와 뒤 행렬의 행 개수가 같아야 함.
    hidden_output = sigmoid(hidden_input)


    # Adding bias to hidden layer output
    hidden_output_bias = np.hstack((hidden_output, np.ones((hidden_output.shape[0], 1))))

    final_input = np.dot(hidden_output_bias, w_hidden_output)
    final_output = sigmoid(final_input)

    # Error calculation
    error = y - final_output
    errors.append(np.mean(np.abs(error))) # MAE (Mean Absolute Error)


    # Back Propagation
    d_output = error * sigmoid_derivative(final_output) # 출력층의 gradient
    error_hidden = d_output.dot(w_hidden_output[:-1].T) # 마지막열 제외(bias 제외), 은닉층의 오차임.
    d_hidden = error_hidden * sigmoid_derivative(hidden_output) # 은닉층의 gradient

    # Weight updates using Error back propagation
    w_hidden_output += learning_rate * hidden_output_bias.T.dot(d_output) # (가중치 변화율)
    w_input_hidden += learning_rate * X_bias.T.dot(d_hidden)

    # plotting the error
    plt.plot(errors)
    plt.title("Error Reduction with Adjusted Learning Rate and Positive Biases")
    plt.xlabel("Epochs")
    plt.ylabel("Mean Absolute Error")
    plt.show()

    # final output calculation
    final_output_adjusted_bias = sigmoid(
        np.dot(np.hstack((sigmoid(np.dot(X_bias, w_input_hidden)), np.ones((X_bias.shape[0], 1)))), w_hidden_output)
    )

    # Display final output and final weight
    print("Final Outputs : \n", final_output_adjusted_bias)
    print("\nFinal Weights (Input to Hidden):\n", w_input_hidden)
    print("\nFinal Weights (Hidden to Output):\n", w_hidden_output)
