---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5U4F7EJ%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T122631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJGMEQCIG04dh2krbou98rm0wmydUAlFdX0lbqk1JtH45Cbh%2B8bAiA52bGPPSYllxtZBQUh%2Bdl5%2FRp5m8TDClLZ1d5LgVJInir%2FAwhAEAAaDDYzNzQyMzE4MzgwNSIMqizYx7GU4wJ1CrdUKtwDWVepOJKnBrgM2BD6SWHAo1Tv00ptzm6dcMGjm5gD8zvoU9BZxrAyvY6o2TnV%2BOmdcrflC4suF6OFqtFca%2BCmP0Liimhly%2FsN02YuJv9fwBW4q7tOeZOAvJhatjllupreCPnyodFsQ0eSHOWGRwrv7Hb867Ro3iyuBk0xO4re%2BAiNbsLP%2BJuWPBbqgvlYVvR6wnBTZF5Qqse%2FlUKRLRvzvWNsoa83e9HnO4Sihky20DhQohDufGc9RSnsPr6FjKT6xMJaOAkng%2F2TxTGMqZ1xLuoMeXB5TZuVahAURfXRUyJ0IVIdAQfFOrCkjFcKatHFyeNOsUHG4lQKfD7bc8zFIBjoSph3wtNy0m47ylY%2FnmyFvF3fve1ir9K3azdhuZgquWnhQOIhuQhThbBv4aZVuZ3AHvP5sjj34roQ3n559ixe%2F2ISGa%2BfAvRO%2BrZzLzSA6TkoFYweVaeWKQ3jabEV6C5zAtNxsqtCavW%2BFDxs1S%2BbOym6exQi5XFP4m3fCi8WgNzdntA7QHbKsKgRuuDURvhzGhQclQn7dpw85gdcagvhkPfc%2Bx7FZ%2BhUTfjhUMPMKSpS0U78hoG%2BpMIHRQMPUoCoIzNFSFquG88xTYp0R50NDQfTwNzvEw%2FIThEw3L6z1QY6pgEmXvGNjg75ozyTcIdHBo3FhpEq4IuxpKajkWIItcxqCppV6JctQFHymg7F8MOKOUd2cg58tGidBjFReksCahCuNR8JL4NWb3KZXSK4AXmE1jFWNUHlc40fbTxDcH57n9pjpm6KLSG0NDBqSo9HXbzBfBT0e137N1gfO8Zvp4aLys7CFrJlZHoYTo3hN77xKGMjdty7YHHaBB1YL3Ta3VR2B7F4QZ08&X-Amz-Signature=883ce13e1316f6d0584410fa12f700d577330d9dc7044137c574627052a17cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
