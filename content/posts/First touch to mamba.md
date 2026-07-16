---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IQEQOQM%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T044914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDQFmvMDG8sVQiaTXvVhLfYojJcJdR%2FSQwskvrIYsbsfQIgKezmeQ0Wpkrb8v42a1aCd6pO4XNSyOHnomDd3XVf%2BoUq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDOpgg%2FgA2OBhCiOuKircA3rQeEazo7JGKfa9Ogw3M8j%2FcfLiX2TvLc0r5gKbOIP0yg6xEmh5y5JR5fLfeCnEgoOfBEuMl6rMi0XYHs8rlT2zfXkpXipNAmoksvkdRvU7lQxVtjRjBI1O4h%2FQqThj619P7zWnrYg%2BdERgzRKO%2BQRFGkNscQ1Q0sxcf8h8Xe8QfVyuoCY7XMq8sJ4ta6yq1l8Jq8dMh6KbZkWAXYOV7h37%2Bt3RXHIGTwb088nagQXCi4lIRSvgu35JZFnu671BMeSu8088r1wObxfPGZt%2FcR1Z5t61rF3hXINSeK6OHbRi34t6DUkB8wGQsofR85M1ceNNMIGezWTtK0GTC1Kw9jtRMWNh%2BFx0%2F%2Fc4yM0xJm83BrPPjAiumA9huDS47t%2B841VGpNqhD2xtZrPtXgU77KEj6kDQ1%2FFjuTsWYKwubEH5QdWsXHK3RzDQ3zO9Moj%2BVVun2Ck%2FxNqmvSB93TvhTlfsqtbO8azfEDCIFWGkVZ7q0x6jQs355RL%2F4FaxdOBIe1QNT638cXjrXTCQP7LeWYAy2x1xFPC6Ej%2FqDg9eCQvD4yKGQS1NBF3OA9Ne95377eOvHk1SeOiSFfUZJTV6rqmByS3RVPZBRkBF%2Fen0RukUURiqjxX02LVs1QAgMLbA4dIGOqUBD4Y%2BUIae%2FuwWqECgVR99QVAPSp86jfSDoeSdpVbON2Qf08oh9fylK8sfFEyG4AY8RS3XHvE9fnGyxehLPiAzChydc7BBvrQyG1vQoNyWABU6y8BWwKjreB5JaavSPp55Td%2BQ6dHbopUQlPNr0FIsvfUN1sWJNaTTGZIJZ%2FCZpJCkNwqwzlDB0LBJQTKkPaKvIMym1EU0ml2QUG1zGJz%2F2xNW8xTB&X-Amz-Signature=1b53e7a05a4e9f72803c39b5f8cf8100ef5015a378de743614fadc0311185141&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
