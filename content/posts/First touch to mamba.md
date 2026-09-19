---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HPDJTOC%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T015815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbDnnIe3rhJdxSEQkRvyhw3edPJF4JwgJrQFjOJQrHiwIhAKbffywz2rQfFD%2FhVZivGubVV2LurohtsE2uYBno7%2FNyKv8DCFMQABoMNjM3NDIzMTgzODA1IgzTFST3Dch4EJvP%2B74q3APZZ9CMQiyDMkeE%2FRk50rB1fnoTs0MSB6LWUlmRhmvmXO4RcyRP9PN425S11GarSGfqFqF1bcqsDHgwVQYtrvVVvGRK13GPTJUXBHAzf6z0sfkosYSS7zHrq1kRQww5dQCDd80WVZYN7XZiLpDBPJeGl%2FRUKs0byGm1CXTKIJkOwazQd5WH7ORF1eURMmBQnpFQDuxjQEX72RvDtFC6UhEAMo%2B%2FHGhJbxf1u3Oo%2BRGyAsQhdzZTPVcH5I3Gg8ronx4EaVVMDbLnvE%2BTKJlhrrp2Yx1UB5u1sfD6HieJ%2F2Cljw8t8opfAxGCVL5nt4bHHfNFBP5f11XjPrWrbXofvUDn27ofan4VX4yKttKycndTmC9hoWVV3DoN4%2B7%2F6QKyBAyY86B9lT1kar%2BqJwedoeyPunZTOFjOr4%2BvGjLpye3p%2FqsjwIRmtfOuS3JoIkhXSiXn294DsiV4ywR27zD9%2BDVX0%2F%2FqEL2lDsbJaCRrVZIIXiD9ys7wvmU7aEpIuAc5BcmNnEdwN6mZWkqv5x46BpCj9giAjogPTVg7q0kE1dNR8WAgE2oOhWyhD94Jy%2FEMvrCQKhKUwt94p2JizEoCAsbL47DtLXX%2FRIdFMn6aOFVqxZpUkvyfjQagvOAEgTC0zLfVBjqkARBpfp9m9JAGSGZmlnzlxp4nq%2B2Az0a%2BAEzvOKVc3yILFn52Mi8gCzQfGJy%2FPJKCYncm8evNz6VV8mNTWTYEoodf7IAEwnz1ZwMJN30kXWwa3i4qDVedE7Uv%2FZ4PW2HevVcJntRpU5bNx9zUx4kteAnJvwagnulgB6%2B2ATRoN%2FctlGgTct56LMo9H1XNR8HLPbjtD4bv8NP3ne%2BtbCd1TeCVIHyw&X-Amz-Signature=b11bb9fc70d02f13eebcd14f8ed0b13772c8f609462cbd985371b979376baf62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
