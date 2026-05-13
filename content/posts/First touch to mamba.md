---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622TCN7RK%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T083208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJHMEUCIDyBkMO6nL90FI4iMDqpIc5yJKjk39oLyLpHOoQ0SXFCAiEAjK5%2BracRhECa%2BLT3LZ0e2Ck6fpGMofDZLNX4v6YX%2FHkq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDEO%2FSJVDvHH2hu01cSrcA2ewnUIHMVRZxoJcJ8y6gxrYPdsi95jDh23nAyCLRsqiqJA3PLoKug8dfOPyCJW9%2F%2BhhCA6%2BGJA4s%2B2u681FDLbI%2Fkwnlc29ffj7r8ZS3maGH77O0CGK7KXyqa6ecLj3DYLTjcq1MxRmbhti5PCrBXfeclxobwIxQilU9rKmAdfbBdmdYbcwbH%2BBzTOwdNaJlBs%2FKDWh9s6z6pRw%2FlG1IAi%2FeLrB3K9uuxFwtawKt6p6gIL7SpiwFnrOKoqcZXzha14cE1N2jnFIsatdR9h9zgp6o4ehg%2F1eCzx87yw67wnT8aZWwOsXPzX9oFfKUw2GmQNo1JoMjvVA9P7ySrxw%2F9w6IT5t3OX%2FiWhm%2F1eEBFkRuFn4nmYsvLkCLXmzqyojDkLKRblVFjF1yk%2F%2BwWR0%2BReca55Ndn8CQioyvCq3FYjqPEli2bVzZPxJ0gheJb%2FeNtd9PWN%2FVdxJDWWuvLg5VP9UN7D1p99pS4u%2Fl0gF4d7BL23xbKQNJmq0sOFpmCm6qZXeQ0V5spsIRhooMpE1tE9ETicWGyuSJ0pWpmKvZEkfBpxHk9JjW06JFP07h8C%2BB3CM2sxW6PKmDhKrj2921ytyC4ptkpZksMrv0OfvGtNAItNydOYryFM%2F9rZ9MPPdkNAGOqUB6LKa8OWnxOwrX3yG9V7jfQbIdEcTKKpiN9CUgpiZ5KpQC%2FGFxrHbzK7fRUmS5qT%2FGk69cl1v3m3%2B89J%2Fl8snsSx6o8ihNcc6nuYrdKLPpthrKYv7V%2Bl7v6YF3hgIHNdOXvX8BsW%2BOqiVM0WZfrcAURa0cpnFHCy8ThVdKtl10zKKZAyyyEwGFKeF2s%2FVRe5DjwAwUF%2BDnUxhk079qYrtkURBbMGg&X-Amz-Signature=dbfd5a85123d816b42b47041f2204a54fca2aefa80cc912ff2f67fd770afa636&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
