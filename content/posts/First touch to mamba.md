---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4AT4J2U%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T215059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQCgCoFjhOWmKCk13p1YfxVSy8dXc2uVipmGb3OFPBtvZQIhALJ7JO4EIzf9yWrKumN0GBo4csmxbNGWDcSUOewVFRBsKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwnK4IT1yP7U5bEHWAq3AMKjoG20IjzA5Lq%2FIIOkwNLnUX7%2B2DCD40ZEHWAqsI3r%2BkyuMOR6XH%2Fol6SgF3UKy%2BU7%2FL1PsZG4qNhWTcgMh17H%2FmlBeK%2B7SMpMY4AlfvyHuF1GYHxC191xX8iWVzYjD8%2FqfTpv%2FiHWyjFdYWmjO9It7P6DzJIfgC2ecKoUUCTJ3O3Y7ZtuySdZCMwe8uGalZ1IowpAc%2F%2BwHKsQpk%2B3YsYQe%2F%2B3HpAqoVacbko15NCX9YOB4OAS06dIhObZHILQw%2BolMzoQt48AJeYhbeMgRIxJM4vi20WaJWTjPzuf1qdkGpMVgTSd0WG1TwHMmtwb7LltdKFrJk7Q7P8iWmuNwZutzTpoK80qWjAzdK%2FuhnickOlmDpU8cNfY5HmaEQN9idRRnMvfK8OG0oxnTmbMTbu%2FZYlmYp2bZPFeDmKXyL3kd7nq0TarT6igeokb8zk95YRVog5HtLieGiMqP%2BKKf4EmVGLnseIjajR414PSHP6MKJInGyW1p%2Bd0oAoUGaxvgf2C1fkwudVlDOaDBH9zZLMm%2BddqjvW%2B5vkQsBGPxKyB1BfsBiFVPOwrC6Tusqcb34CYullotVbGSOR1tibNdXEhSiukaOBgLNz5mq0pyo1Uu%2FFbu%2FUip6xBQzivzDntqfRBjqkAcjYKXXP26%2FGkKdYPTWgYFNiWeQ6P1nfpnFUpDwpApGadI5JXS9cS3Gxn7PRR3%2BcVkeieP1EtIkVMbRBTJTPl%2BUrnUOUXYBlBFZ5QIAkNAPcRwCRa01a9KKf2lTD8O1y36E7oxjKHe29W3geNUGfSica09sXCAkOEDwSo8hfomMkA7tZJqLjPgS%2F6YgAAeBdaAxVIe1WFTa8u3IrJ9c9rz27i8gO&X-Amz-Signature=c16148b9a903bc5ccc80ea743be60ada84b46f284216231d8e2aab70a53bb898&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
