---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX745U5O%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T165035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAa6tj7tA54oYxOeRGiah%2BXmLXn8Uu5xCCdC4037WfVQIgK6qO%2BQJRrLyyLIx%2B5QQEX7hp%2FwQP5QcJQF5BR3SNonoq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDOMYGAivGtguf%2BsJFircA1AD%2BWxElHWlhhRG5KQ%2Bfmk4YFemEWplUrlUkBeIhvFJR0L0WMMAbrx9jZsT51BBXiWKQpprUl6t94ku%2FPdGcu9q6hB77TYYsIZEzqhaHR7sLXnAjPEKqQerS75OhIMCnoWhq%2Fr2R0kvX3XTjTz7121Kf8%2B3ch49xDookFoXvyAxuEqv%2B7pMwHxO4AFJTtElumtc5r%2FBOPNTsz98b7HWvdk3KjI0eafSnhc%2F3OuhoP04oAXkSpO7Lh897QoUI%2BT4k9Z83NGVlzABmmxU9geROJiQfk0EXhg5LtoyFOD25CASUhmau4svxwOE%2FgcV3wX86qn%2Bm4r%2BISPqdEK7JR%2FiejmG5wmuHBwNytsJCtBKzGWz7%2B7irSiVR7HNt3ffEkDcHplaV1Hawr33wH2jpRXO967156hw%2BhM1W2jYBlvopzBSQXRFgeVuq19DwQF4Jnjid%2BpfCarI4I5UM9sK%2B1iYRPn5wkgF6bIs0VOaLPQxL%2BSYyVRenXTDq9XqVH6Kl8qNg1po9vrHx5h9W1IF4shLJEYnTq6hpCom3Kg5yUP3NDVShNa7N764yVrHHd%2BJawd0kLhtFYipOy8e%2FS0nQdZU4wUFFoxv5OtdswdznUnaBrLOVIsrIITcOO6%2BxNyYMJjRzNAGOqUBm4VCrGn%2FAHM%2BPO5slz%2B9nauMyyd43x6r1fwvIyPj8Ua5v9duDRDtQW%2BiGSr4rCUFCbgzGGtMGsgTUpeSZwWlehPZ1y3n%2BOb9VLR5nYVR2nCv%2BJ5wIthvWv7FYlA7UG7y5011nXrdf%2BdwfoWNOeDTlW4buFLeuxklLIIvMJlyovSt7Vgzm2AfiTpE2DJlOaJl6Cyb90nqbOAPgAL7kRdvLr2zHiYA&X-Amz-Signature=9f26d2ac528182e542a81fb76ff62c55052c55b9beaeeea68200ed89a3fb0988&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
