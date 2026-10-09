---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQZXFCD4%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T032309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQDRoJVOBuRc7Ct8jGV3fzqcFubupsy4M6u0y3QmtLBSlAIhAItRdK8TXu0SFysW8dlKY53w05pLX3ntynToUD0dfg%2FMKv8DCDMQABoMNjM3NDIzMTgzODA1IgxRdradt39eE0a3Au8q3AMDo9jfLkEMVaO7c%2FPnLolQ74cNPBH1byguHBlXLQD29DabFkHdoxej%2FGPoq4dh%2BWC87Ftj7UGSHcS8FPRSuEGi6kmgL%2FGzPzS%2B9R5oo2Z%2BVE72fdBYqoCDs7LdtdN0q3a3r%2FziwaG1E1twoJgO5ho8tGooAocAF1Eje0cG3pxpiPhREasMcl9MIiZCeWTY8%2FGFO38TVtBiDlpQyCcTTUsRMSstRgRprDibzu9KqQza0tl0KKyDj47aDTL1TFOiGDz3PO7hNdG%2FrKiV4E%2FG3XLVo1am9ZxvFlzRE7O0kWMTeWO63jPascj0L0jLeqY9v%2BYspzviNZLPFgmlq3LJ7ScPeMNOAAlxCnEfEY%2F4C6GNrjts4fYjbKh%2FS7CZX8vWsSvSWvXVtC7BmDwnm1jOvz9cXVoV2%2Bx1AoYra8JA6liiUEwb%2BaJEzB9Zv5rqGtIw22T8Pii2fJIhLfObIWJozI14Jz1uJAXTU0LLumhs1CnnmOsmU7T8AOsU37E8hvzF0Pcqz5V1uB2bj%2FAKTOZb4R3i32lbFkwlfWasH27N4bUMzqvUtf7W2APxx6tEIlEwYisaR1G3QK%2Fcf5SS8L5%2BYEPGL0rOs6Djh4D3kP%2F1g2d%2FhBb6BMeheP2STeD8bDDDm6HWBjqkAVnzteX6f%2BV5yzrNg6ZhJ3FxSgmfbc3%2FE4OZctpYGx1qd%2BoioIK%2BmLYra%2F7G3t%2BjjgsRqhT75kOwbD94TrQ9LmqhzwnJ%2FpB7PUDywr3dMspmm6rpXVjh1c8kw%2BKBv9e2hP6st4X8v%2FZEw2PiWyJVhJU6eIJfI2dOVvr0Fx7H2g3SDLrE%2Fhw0NL6RJbWJ0zYEXEQDb5%2Fm9cvgjCliG2D5i6feGOhM&X-Amz-Signature=15736f101241ec26026738c37b4e16bdd2454d30f84b1dbd6bda7855a70dfd2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
