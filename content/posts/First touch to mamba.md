---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJRFDABS%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T194438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA44sl6g1h3WuniyQ1MQDf7I9VLYxIra6%2FrJ0jWwnh%2FJAiEAjNGNG8Uitp7MuSp6yogXv2nQj5sOh00LIgSiROGpdCMq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDNNiCSXozibZ40a8kyrcA8mHgE73doEIvyN479ASVoKReSh8e1UTmL6QF0AameDpW556tlOkdbJYwRhGpTZjOJ4wSILzIDIHqLSMSnpjDUN3Up%2B3TngC8vCwhG%2F1swtV%2F2hvDX%2FuHg%2B380ctQF7q7j0qtbIvFZsa3zyoDvFxTzpvFMHIUHhSX1qLvlr7ZzKzpTWYfjWmWYDyIao7uKwpvPPZEALA7KFqwoi9ywFlDEN8IoYR7F%2FxI6sWAXmGc%2F5ZdoZcvXkZbkWcTuKQtpUUZegKLQH1Ar0d4rR9bQozdEATvErtj%2BmSarOkM1Uc8dd%2FG3%2Bz4S91utTnMHbaaQTUM5n8RV6vmW7ULVsJxUBPT3WIAuxUtJB6UBB3xFyJamlf0l%2F9oJgvVbtfcdOAgkmhSPbCJL2vjHjKhwDSU92paqRHXoE5cy0fKxnIVab3aFV9jIKGtVgcV0XNEQfSBIV6vksIZVjQaKpvm84KKMzDjbbb78bCggsBIKGZQEJ4unTzXV36Cn1KA69%2Bkywv0x1oKU7oNMO5B2jvo6elVU%2BckARbtxrDKSoExE1h%2BfJnHSxSfZAqPF%2FJIcY02k67Ll3PzGqoOqLrvgd4Zqba%2BuTVBLha8QhjzF5O%2FhSziyc7Sy%2Brgd5sxoB5Ya%2B1Au%2FIMK3Z9dEGOqUBEk4v3Dj8shRjCT8JRUseO14tCVZKhu60ebNjgmTw59KWwUza1biUz6oekH9ciN7Ebr9CetvYf9Eq9EGEI9m%2F12Hoh79IMu3LJSLz8S1grts9X3ijyuGxlPFtSpdkT8I7pqM3C%2BQ%2BxjwmXoTTWd0Bi1VMEl0Eb%2B3uSJZgBAAmImF1gm9mGTyAtdA0fd0zqf2UmJQm53OVRybNmz2NqTFHcJ20a2TP&X-Amz-Signature=3c76a29f5c56ceaf9b0e1b890e0a69062e4a9b97aae48c1dbf4276d5d601b2b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
