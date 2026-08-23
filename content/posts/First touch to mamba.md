---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHDIS2YT%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T025405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIGGGXTk0kbAEhwlqOXUL%2BRPEGmAXa0hLivlSClBuOeutAiEAmFnI0z%2FJ5ga0FRiRSF0YgtSHNkZvFuCbxcbUUjXe00QqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLP%2FaZsDESc5KmqoyrcA2OZXrSnnCNxbk6pct5u76UCEIFrR4ys1zY811%2FNPl%2FdUm7mt4xuvpfTKsna5LXVpNLKN4AApRPAdGSDImNzyYGI0wPzy7qxCDy8lDIUx8oXzHXA01A1RJtgO6wcuSzpsqHG6TgydcffNvrzMyM0ESR7eBpzrMEZFNwYVSXKPF5kWRxTdcrlSMP09Fk2LHa0OVwV%2FF4v%2FUbwWV2wwWbkjhPwidFIMjAIamCyb%2Br9%2Fm2X5rX5gAbWOuGe8CYyokv215GDrE9uKW3X8Zkif0HgB%2FSs0igzV%2FZIDH%2B%2FJae1ZR2tm8HSj%2FQzXafdGm%2FEd7UGVMky1bC32DcgLswvNAfLtgQK5IuzvDo%2FsewrnV8F5%2B6LopuVctZ%2B0cLPdyFM1Yh0QEMm6JZXa%2BZByjnZ3p5d7tSm8jwcFowNULolF8zmzHSMfZowoSai0XR%2Fl8tOM%2FWUoFjfCWoUoR6VVx094wpnNw%2BiPWKZkKhIGnUO6co4bL2sxaqHdNdkTeK9yoAn6C4kQuvFB2Whj3S9sVNQW%2FakKmg%2BU6aUgbSdwVAYPlhYClFHYf1FP8txoBGUu4mpL63IaIHg4GnAyMVqoZA2txRrZw4ojtIyOIIDR5nEalt3Z5daAyF12c9F1HN%2Bn3vFMLe4qdQGOqUBLZtAt%2FttW8U3HdtIkNZk5YU6fhK%2F1Hp32DH%2Fd%2FLWsFNMWTsjk4sbbtOJwT4uW%2BS7hmbhbr1TrG9RqzA%2BsRy7Pxe7Lg3lYuAzD%2F%2BoPy7jt%2FMUpWIGf035JSNuKpibOHK1z3s8wcuGwfIJq7%2BN1tvMdYD0dpCe7%2FrmlaiMrdbCWFu22WaaxiPouW%2BeOVwHde6rYXjT5WVuM9LAvSWj5WqFJn0de8e5&X-Amz-Signature=943cc4a098a9128a21dfbb7526c52ba0f2e369298c793382e9d575882b2b0051&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
