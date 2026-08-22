---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIAPZZ5A%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T081628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiAyU4hlnfuCuh0xFCLqbEYQbTdPuwAcS1zsCCwZdY6AIgePY11QQYnfLXSj%2FAtry9%2F4V%2FjClORri3CqmAF6yHVjoqiAQIuf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2FuSDdRIMLNh1AjjyrcA3BwggErmaH1J%2BSP505td3iA%2BTCn7j0rHcSMGuBXgFgFDXlbkoluuYoYbf1u4irawmC2Cn6zFTjxjV5lCtjAazxLwRDbNLP%2FprweWpNOlOnEpQhioXu%2FjhblAa5ooHXuuYDCkGkwqyF5JD9OvBNXJzzVmLil15nniKxtUUflUcKnPLX0%2F2O6J2D50NQJZkhGXojjkgCi01U%2FbEYfx8C37PDrbfSpXttK6RSFNVcn8zRMrmRMNMKxqdO%2BY8UbTZuluFnmi1uxhlYSAvyUn0Rql7ohX3lAXl4x9fzqmLwh9TM%2B55DgnYAb6SgvBkLZOCpJ3aXWtNajVjeL3bZfqmyS16eBvUAt3FQEeUP%2BnAAGM5cOE2DZrt7l%2BhGpgs7A6GAVMMWl%2FT8TZ2TkqeIb9cxe4sfymRusDBnA1VP8xZ6PbKtrfCqK86XtWoeUTw%2F3dzzXoR0dMBkZKNwF71Z1MXISbHRhizb13FsoFBK7J4YsfkGRvZE3mnSG0cag%2FoPQmvV2RVVhLlEuqU0O1MnzkO6xw6uy2ubh1iq5yhznKBA0We8WWSI9UqbqZDKGa9yq9IGkUUEU%2FoFeDaI54Sk%2B8xQn0nsm0OyNEtrBYjsd8x%2B1mjUxUmlzBgSsSL1QrtkcMPWupdQGOqUBJkypK3g9yqe8WPXlLlswKpfDoYbxGbhaFKa%2FdpV5mqBpW%2BNrT7Q5wlI9FpGYi3ywRUim8kb1C1pYDzfSVhgiWNvIGenQfjlqbS7Q18I2v4jBpVupOthqhATkq6fkVfzZzUAVz2Eu%2BOUqQYORxu4sdya0rdG1XgSjMKZwD8QnGavkuO1ufbyXx3nH7za6OEp5T3wq8%2FFVDrrNCiXNzIKU%2F0cyJto9&X-Amz-Signature=69a931604adf6211b97ef4f45ca5b16a73def91704e5ada3ef70c5a01ed3f243&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
