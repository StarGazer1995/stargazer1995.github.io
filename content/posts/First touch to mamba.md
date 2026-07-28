---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4LFCCWC%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T081202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBB0iBrwi6l2Vdizxg7q42aNGq3XW%2BBCOfPSgsIeaI8cAiByo5XhyL%2FM94Q3LYRgXj9wDDa%2FiPnKsF3Kd64hk3ZPeSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMGfXaYxsjCKK2lGF0KtwDlojnNqYPOfE6tdsaKAzC3uWw6zacP%2FJBte3Vvrf2BFxq1gLC4cFrnK871NRGja2A6QpLbmVCu%2FUVr6QRJkx00ntaYYDg4jL14o%2FscHetETRVQH16fwlILU5yVpdZ4dFl1IOEDILmufUgPcpIeHmFctIO138TLQboMG9A9C65%2FExLFX29SeUlQEJQgLIbl8hrxN7FipXbCC8Ugclz%2FEnRUwteGZLZJhEUWEUpOLcwIhX5f8JUCev8%2BKdEbrHxSQxwdRY8QvwKMc5J4QyXAHGR3t2yOdl%2FQ9noN1EnR9rsgu0TbyYKC61GiM38k3OWKS%2FLJWorf4FPOtyCH1imPOz%2BOhdPfcr15CiO%2BUiGM%2BewosgpYykMPwD96UsuNh57NF5gt%2FKVMa5xR5XRaKrcV%2FBPNLwUVN5enYkBuijlBWr57L6MvkEqQpmGwAwluxLBFJwXE%2BIvQyINv%2FDuuHQt%2BSE2AnUf%2FtsvVsfDpDpXow0dtng%2BAIXeKfoT9vtVL3qTuvWx0knVWyIJAViWos2gOGyJ6JrTxe2u%2BJgo6A3nFOM3vjl4Re6uYCSBUUctudfwsPcHGRv39Ybglj1t3gVmi7R%2FBf7tk2IdmwiZIWw%2BTB79eMFW772kc3dyAR0%2Bt8Ew166h0wY6pgGQGuTa9nh2MDBW54KJEV1qXchpwawX0YFEy%2FfNosnpRzfWr68KfizMKdRO7JLfW3kRSgCEvy4pENwXGy5Ri%2B12Bvp%2BY6IacG89c%2Fu%2FB2eQ2wDMy4AMmpXNrzjKoZ%2FLY7nT2alTf4wVfjfSZt2%2BP%2FiOQk%2FGIH9KhXrrXWYyQyRxUKf9mR4ao32awtze4IvzKm%2BXXRNyHiORIDNFOcrP9D4KUvHEyO%2Fs&X-Amz-Signature=6cb6e9157104ac38fd3532ebfcf3bbbb45e006e64a34270fcef081e154dc473d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
