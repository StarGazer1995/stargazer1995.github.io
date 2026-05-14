---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664O5JGVRR%2F20260514%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260514T192700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLW6l%2F7RbIj1xub%2FXEzTJ%2FpuRlQKfiM3eJM%2FmqgmZcTAiEA8nkxggYlEdUhOd1ETvk3MVEShm3GIEKePNpAOVEK9pEq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDNK3e3ak81UI4uYHeCrcA1Vxz%2BdlTmhhkXs0f6iqldNNgu1BLm82PaVKkHjgAgZ%2BpxV8sQ4wbNjEMGv1NjSiy7HBRT68pPIAsK80rUF1H%2BiKLiNYBsyGa2%2BWB40BWWD0lZUIyACGBNmuE8tpp%2F6ihSAxppM7B8zh9T18kMkJ5f%2FhmLoBIT7C2X2KDqjn%2B%2BRVZKA3XE9FfCOQ8lT3q%2B5sE8HXxcgew%2FC46sT4ndvKBALGZ9UVLVfjbf6vLFK7s2yOrO0B6e%2F6gWeAGiFRS5SQeu2IMVO0ePY%2FoR9VbGvKMYcb1gaY27HBoa8Y%2FeCl6mnzXw96aJ67qE5kRzKCt5oGO4kZs4FFU1zic00EsvCeXczH2%2FBy3DI76%2Bs9yaUutifPqraTmjRhQSxem9OnI0nlHRgWnx%2FkXOAhNBdWaJL4m2eQIjeiQv0m1SrlTZXkfxGqXRhoYjwe7NwMhkARFaA9R%2Fdk0J7IUX9hBfmqqr8nHnJdEQcOV0PyNRyhBWkTHZK0QS5QmGEt0hPmNfx09kfUx37TJqyIGH2S8joOxesHSnxAQNBr0f4D65VraKKc5hytHNwWrP3Ufyo9H4OONGH8oKmq8SubiUp0zSt5YdHwB5WtU7QJ%2BzZV1MOZABhPDjzKl8g3YnMSfufM3WS3MPGemNAGOqUBCcJufZF4V2o51eh7hhFr4KB%2BMXDN0Hmqk09OOlVn5qv2VfY9fgxpo3zLrGay%2F3irvkZNblc1zrlDmQ%2B73N2%2Bj8Pjj8WZ5by7Is64BESJ8trbZRS0Eig8HVWXuElImvMcAweOQJegJpH52cixAABQcIXpg3PQlKckajJ34qAaGC%2BtkK88hRtGoV4bqnY2WN08FNdFPm6RKaRWeIDil%2F4eREiwmOMG&X-Amz-Signature=ee2e2301c1dfab51a6188bb467c6b8fb4a55027aac3ec34e68be088ec58412d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
