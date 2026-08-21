---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU37EVJQ%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T082549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHsiOfQ133Fc1hXtuIsC3CGoRuccFd%2BMz%2FdvjBlJGg%2FQIgI6JMB5GzfVfSGmB1Uk3ECXRxJFfuHh3IYFuoec1cocUqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHmR3R83QUBKZXwbkSrcA7rEbSA5fgAFdRrO7Agczt0wBBeum0r%2FBbL%2F0hR7mPMy8EYQ1ScCpmqvN%2B7YJWqJ6qplIv6ZJjDLsYo6dW1Py7Ix2vihcA6guzhFM9Qfb1jUA7tkRgYAl0%2FhonCXbXxyi%2FObRQBPX8mCV4%2B53w6abMKwkBBKIE5F4qNUsuFTa98DuPYA2hfMZbUizC87oDcOGw4GVZWfJQ9il34G4HCVu1Doefs9KSovPV%2BWZ4Z0bKvlztUG%2Fm%2BdOE3t37cXrnFCp98CUINJfviU7qr16Df8cXWnRZKCTWcU%2Furh%2BkBE6r7E62Lw37ERlxWfv01GnlD9gOx0JSyYf6xaezy4cNXHgkGl%2BmtBZgDGdEY3p1%2Fz7Lp8XKxw%2FFzxnHzjKCJA0V7KkM7s4Nw7xAMFLuNQhWNA82fwxDqMEL%2B82SLkblfBPAFWMi%2BhvW%2Bx%2FXvhvPvnAJK5wWhmcz%2FGnmSJSDdYVGhbdndrJA%2BQrbJSeYgufjZR8T%2BPl9uHvKQBHVifVSkzmQhnE%2BIulFFeZkeraazsz3klmGkAynx9G8hHmQQmFFgXY%2Bou0Cjc%2ByqD57kKVddPvi8X7VWNRxMckuYuBZwvuNrMCGmv%2FtDVeU5mJLTmns0s7eD390MHlMl7s6sofA1bMNjon9QGOqUBkQqnjNjCZC2ISQr%2FoBS0vQHHcVFh4ATqTLEO4MbPVYhsz7oHPmG1lPAlM%2BuiDQPlNzLuIlEqpYQ%2FpsUfwXezHC0gZs2TI0ZpM1kOrTdJdlZHl174l3imEPjO3LhyctNGHeN%2B9Jq4W%2BOtnV1m0%2F2s2js0SK7yBDG%2B7SkLVlLDzZ%2Bn1uhIKL6AFlfa2fa0Y8%2BMGYnKqJwJh8jiyMd3mrje5M8qHnzN&X-Amz-Signature=4aeee0d1cf8b2e9c813a8c9eb223c4437ef97673cd227d1c1257b1eadcafa3ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
