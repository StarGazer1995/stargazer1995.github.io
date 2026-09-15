---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWMNLUFK%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T234848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCICOZnrdk4xUNxZGdDj5y6tsGSFgeY3ClBT7jRt9MFlacAiEA5g9HpdTbUIdMKVdiIbzDJSsDZv2E9Eq1GxjOelsp80Uq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDJom4B3xHpiH%2B0tNJSrcA%2BV1W3RgUcgNCfKvXvf9F7PmM%2F83HVBPMyBoJfGsK7qZ5rNiyVoK4d8bcL3VCNcZrKYadFp53Szzs56rvzeq3hi5rUueLHfgeCnU3UQ3oadzAmrhEBTLcZmnwzP6xxPBuvruZQL2zvLlWyvvJ%2BkjvoKpmmfhap2pcXlxuGTg9CokTvIz0gDxaWtS%2Bwny3HV2HoY9W%2BGGRa5ssHo3PnsyVPJI9%2BgCK9BNAaSNs166%2Bvx%2FvWtyBGRi5Ja2zCNjVQOgAWngDzPwGfpzIRIkPbL3%2B1xoGo04Ai253IyOWnj0puyD%2BzQ6DgUdGyjQqO2XeUpdctwA6OJB%2FVyGdWCsFgqmPoamUXkP0w3XkN02Z2soSKw8ejPm4jbz0cOxPTw9YrWR3t2so%2FCfO5JznjYeBSAgZ4qBVaW1XTpAyj3Bi3Ns1YhLtdKl9yMFGc1gjp58Yjtx2e3%2FAh2AvHslrTUh0qfLKK%2F53d21%2BRZtnE6juF0YZt5n1EzUZNbOWwg8RppYroQBm%2Bd405A%2BHtoCed%2B6jlkOYQm3wEZK9foEcSR4xlBqKels3X%2BaLLeJbD1Gi7ijoq55Z2V8w2S3a9s8YQh8Rh02MTa8NEo6BS3o8fvsg3iYYEyNloUGI3lDIMfyDPewMN%2BOp9UGOqUBvUs0qgosvpk8fA%2Btp37KwscJjl05fMf67ah19uqoKTvHFZZN%2FkQZumRk0a2VxP0YRdNxw9fDGDTQU5wHLHM1pToYO9dt4sWutoA8LBnf0Sll%2FbC5pSsvLykXr5vrhrd1jiNuhn76gaY5ZADptR2uOlbw%2Bq5X5pZGMBehJ6WR7zckiynNCJwlRS%2Bd8kQcyidhoT24qa5ANtPyE18SomoJUbXRsSs3&X-Amz-Signature=e29985bf0b62b32807d83eb61173ee483436e67d1e392dab5f2482b08630ef8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
