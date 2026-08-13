---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRRQ2OPF%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T052930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDrNB9LIyhMMuh%2BPQ6BxBKKvxY%2BGRfDjmteHtm51ZRKAAIgEvoVPHCvDhE%2Be%2B2xzx%2FOaE8uNWwXR0AV9CH1iOQrhWwqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKkn1TnsL%2B3JhTJwSyrcA6AZDfy7g9JZaQ5H5C1CcK2EQg4To99o4IIMZPnXsb%2Bz%2FjuUskCZj%2FMs4Gpo0D4Dujr7gNuYMTJkmuiNTt8Ym%2BWAGEz5tXATLgp7yxYmbiKubgBfDJ7DBQCXXbExVnN6LsYi4%2BBI04Vm8R3MGTY8rBKF%2BuRwKLA3HjNX79WE9DalRT0%2BrEeKtGotdBk%2BYt3WogBsiiDKcUpfS9qzaCvly%2FSK2LgGP2gAS0P7CofItwjrk99Tkm2Ugedf0rvZqxVj%2F9M3PX2nKHy%2B%2FGTHcqFjT5aHCWOzY31Z5gOA7LbtP2wbPrQi0A%2FnYVbxuFz1%2FVhbRNSOe0eCjE1ysekmKOQSiCE%2BdVhckfQzmCpnVykaz%2BQz75CRPfywtcQCzVHnnADUfPRLxxQwHUTfmUhkUTPsCXmNJwdaq1MTwgicvGh4QwgvtDfQwk33nrIAD7%2BGkVjod1bAJVm2dcrdYDHXH3R%2B%2FofjYs53%2BGDLr2iIi1Wdwzpdj4kYzjkgEVQi%2FMBaZJmBGmvnE3ae1CF2tJx5IKhaNjGBoXAyJjLjKdmIUOqtnS7f1lyxjXYlEme9%2Bd%2BXmcxqRAr2I4cU5Sy3YhYnwuft%2F9422vIJC%2FnaLT9Qf%2FDBn%2FukKNf9hIRwO%2Fxzu4XOMJfG9NMGOqUBptaoYmP4FjqtAkRmqXaW8jiXqs37d5oEqOGZlGCXX7SnMB%2BrxQKvUGwMVEMrT0MmsPaH4JPwJb%2BEoUgEMhOlpqMLmb7HC0sIP0%2FCaAfWBiIk%2BJjsyTOZqwZnYzIWTcCgbIV97IgsN%2BaGTttSxMjTGUMGOatSkc6TZcbovfTaiqdCXWlvvWbbuqeDN%2B%2B4xDS3VbhxEHJuSk7fIatHG%2FdPA0UUvz7G&X-Amz-Signature=03d4f893dde6d357a2faac7b6da0d137e87a695e83180a1715f0eedc2c08ede0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
