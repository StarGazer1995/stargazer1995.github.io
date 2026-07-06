---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIBYZZJA%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T211947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCH1twysX%2BUVbY%2BEf6D3xtY8Oaw6HpLqtKWSFgUdEVzdQIgRGfGED0x3Iee9F9QJPihBACi%2FBypya9N%2BNuJSFHg0Zoq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDPnqDrMIB7wu7J%2BRCircA2ujyUqjRLNTndRqCQWYXRH5XEBMSipVHPEZbwyOrhb2baw7cSUYWzwOsP0KAlYM5QQJcRSVNoYYuG4nSS9YBrYXPfmvfmGbOHmaG3D6Do0Dj5MPb07EyqOW%2F1bWLCKKn9aATGyV0VQVErQmTADbMYO12qTsmoQVtrIuU%2F4hpOIA6QYjiLsIhpmfL7Z5tOfRj29CqMaPaLi%2Bik7y5g69U8yW9DiaIZ4aNqQ%2FfMaImHeJPXWMm6gTZvBHAxOUn5M8l9KifxHGty0dNkZxUgGDDeg%2BtJmkKl5Tu8S%2Fvr2kYqnjgLSj%2Bn0yKSsgx%2BnkByD9mOu6nO9UMJ6iiTn1gz0VylKoW%2Fa3fDVh39cCe%2B%2BRggnePuXa%2Bnpg%2B4YsD5adRoW%2FnpmuchahigzxgkGnsk6YAw0%2F%2FiRhJMb49YkDVa8eBhOlGElgIMerVrPybXOA3r%2FGS2Sh2bq1FHEL71fimG1uUlFJU3qo%2BS%2BRuNHuNQWXF3tRAa7WlgQ2Z1qmgibQrEvGmAgTSnQtIRKnLwHuiMJAygx3XoohjZ0m2G4N216i1u2q5uoGzlBgPaUS9v6Pdlqj4LYIfLdYl5V6bJ1UgF3LP6a7iKv5j1RXsploDSh047YCie1viOFez1y2%2Fdq4MNuwsNIGOqUB9krk7No2Thr%2Bh1WkRpjkZ3bVzYV9LYxlO%2FkzBKPA9uHwm2akyDdcR9xlgVANiTcVjFn04F%2BQTStjn4LXYDM7%2F83hGrG%2F%2FmqkCDgQWL4hZfKKk9yPPehRyVboLHjfBJu3Umgdl6LXpYbqvhLfxwwCi6Pqua9s1z8%2BkVuJGuErL3TiVzos27cz733y1QNJ82weezrHL7O4KL7pJBugnF8BKegn0h%2FY&X-Amz-Signature=ea65a6318af39bc584773059ad4862abf95e55bb51882401af8371ddfcca9e20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
