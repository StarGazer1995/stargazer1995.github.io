---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPXYLYMI%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T224637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQUR9LHMSNbYgt9rDtjCg0Q4DDBBsBSWvydy%2F%2FkiJW%2FAIhANLoeMyUBKhQhlVUkEPDsJFeJF047PWwsHoUbD%2B1o8oeKv8DCE4QABoMNjM3NDIzMTgzODA1IgyPJUtHlFVb6D5WoVMq3APZS6pFCFKon%2F8QL8XcImLir1oku3hZIwXYbRnlnF%2Bn42kEqIelpVOjxRfusA2yiS6g1R62MnAmsTr%2BFk15vqxZzeVh0n8SnfC3cKNGcGcGsNpZ6penFFJHbLEY%2B3eAtFKYUnrd7wocre0vHwmGZN9YWubLwTND1FD8M%2Bp0Pz9S76Nxzv6fULbYwa1mC5dLtYUHmLOWgBrdiIxS1SZJ215omQN0%2FbstdWe08D%2ByCls0zV7phCsT%2FIGScszjY4wOKb2Wa7ijPwRnTGN7p4PEnrKgI6QpEK0AW6HHkI3lC4GK8nIw8HLef61N3%2F%2Fg0F3BfLuFk5Svc9RTUbGr7a77iscFTkG8SyVAOeugnS%2BRJ7rPVmFAtE%2Bayf2xuFKSwO8cKz%2FM4g5Q4ynz2TUYxytcZJ7sZf8A99UsHLAaBO7puU2vYZI%2FaJMNs8eXCQeP1hNMWjNaKsYXC7uuB7KNjVOuu%2F8MKA8hdY7oICeA%2BDs7r%2BVXGxjSurAo3yf4OKU2nQj%2BsEtB0JnrKKNUKyR5kfjnCHX5mAV%2FAg%2F6yrHIpvoU4YWbnlt1pdmar5xBS2E%2FIx%2FPxKbaVgUj9Rv2vmmbowNqbXnpCP87jL49StHIc6OS%2Bkv6Pjn541jD96w%2Fzi9wITDkiuXSBjqkAbg%2BkWZFElncZ8%2BL6HcWRPdZWCo2LClcozgfQdN3Tgbi8EliFpu6k0TQv4YKyEY4NjJnlfXZJsi3tqai%2F4F0rWsXHFOyM7O3Ty2SFMUP5AQn87ECPVi21kGwFCD7IxfUgbxvam7wUxtCmypWdkfeQmu0d9%2BHRYkaOVMm58C1J4NQc71fij6sBvqiBg1A5QcDsxSapB55e7NLemMWTZ9TGylfgKwy&X-Amz-Signature=68d9e8b24feb55f3df4b13e62ac39819ae52f817d603346f50bd117af60c9d09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
