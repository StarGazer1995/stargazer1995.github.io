---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHGWJB7O%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T082744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIGdPwUv9W0v66uRmDbXOtwbwF5asecYcDKsWiS6TE3VHAiAHhq4uFDpwtfmqnIk61VfQ77itCxbFBuqHOnAYqwR9OCqIBAj5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeGIzc%2BcFNlap47CEKtwDz51xmPMmMIYB5zt70Sp5MwWChJ3jjHJCWVW9iyaHRYMMZuVLJhAxD9bKtOMHnbFGsJZPquNETJrz2yPp0JLTAowVboSTEkKI1xZxSIKpuuWEKayNZ5gZMh7k3MHxTHpz9ajEgB87phRI8fzBGuzX9MTZI3nEz9%2FvT1xMOLSB57yrKBH0unD%2FkzRKkzb94lRQL%2B%2FFxb6a1Cv7ssgbSjaKKb5n9Rw%2F9U27aC4r%2Bbl%2BZEiahTHZqpfkwgSWrdjbAuwD2rw56tsvJ%2FyQS4GrOMZdNHr2TrBvhj70FaGJtCOkUsFrtdfb7at6SQmYTERvJXY27utUED8rRJVYPzHpUKkYyv43Utihr3%2BicxWn%2BLM44Lbty0dw8r0Vpzg0WBIMIxn2FZ%2BROYKkVikb0dApAHysap3C3gsKKbxpPgIz8ANZRkD47akckgo%2BmeesgEWJYCDLR0DqGVjsT08NEoVNR4UzGNdrb6MrgPynyJPyhz7x%2FNpiohJDxOPToVoe0CeBUGyEIm0W6LbZcXEpOprWu3X1zJZGmJsArc%2B0SXRoGIuDtVadJWFRcwh27C2o9lZgP771Fqp%2BLaiLDGoXzCpyi%2By3EVBeUQgOh%2B97cEe45Tt3ALDgJAZCCDV6v9unIuYw4c2p0QY6pgGGEgam%2Fayn639uDTeO1sINwjAnfOakqvrE5qZoR12gh%2BN0qlVEo8yVvnpX80nYWqvo9ly4emIa7N%2BRoyg9JxoyGWbhq10kHQmEtGQ6WI3x19IQPopB7gQT7NW%2FjXLQytKivEAcgyMcN2Fu9MAjn7VrHXAw2HpPkfd36M5sfTh1WfQo8ylV%2B9LA8XaAMjk2n%2FsRIUm27dm2DxQ056t0D9JUmiWtoWyA&X-Amz-Signature=58d902479d3ddbabe5c7158b6202db7407785a087f0c17ef67b31fc42f7bf90c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
