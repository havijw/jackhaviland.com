---
title: Forms Without Vectors
author: Jack Haviland
date: 2024-05-27
tikz: true
---

## Centering Forms
I've been reading **Advanced Calculus: A Differential Forms Approach**, which centers differential forms, rather than tangent vectors, as the primary objects upon which differentiable functions act.

ACADFA's development of calculus as statements about differential forms in $\mathbb{R}^n$ suggests that we can develop the theory of manifolds via statements about differential forms on manifolds. From this point of view, tangent vectors are only of secondary importance, and it would be preferable to construct differential forms _intrinsically_, without reference to the tangent space (the usual construction is multilinear maps on tangent vectors). It suffices to intrinsically construct the $1$-forms at a point, since from these, differential forms and higher forms can be constructed.

We will show that there is such a construction, that is, for each point $p$ in a manifold $M$, we can construct a vector space with a natural isomorphism to $T_p^*M$ (the usual construction as the dual space to $T_pM$).

Here is an overview:
- A standard construction of $T_pM$ is the space of derivations on germs of functions at $p$. This is kind of like a restricted dual space, so $T_p^*M$ is a restricted double-dual space.
- Since $T_p^*M$ is a subset of the double-dual space to germs of functions, and subsets are equivalent to quotients in vector spaces, we can view $T_p^*M$ as a quotient of the space of germs.
- The quotient identifies germs that cannot be differentiated by derivations. Intuitively, this means germs are identified when all their directional derivatives are the same; equivalently, when they differ by a constant.
- So, identifying germs that differ by a constant creates a vector space with a natural isomorphism to $T_p^*M$, and this quotient of the space of germs is defined without any reference to derivations or tangent vectors.

## The Details
### Basic Constructions
Let $M$ be a manifold. A standard construction of the tangent space to $p \in M$ is as follows: consider functions from neighborhoods of $p$ to $\mathbb{R}$, and define the _germ_ of such a function $f$ to be the equivalence class of functions that agree with $f$ on a neighborhood (contained in the domain of both functions) of $p$. The usual notions of addition, scalar multiplication, and multiplication of functions are well-defined on germs, and these operations make the space of germs an algebra over $\mathbb{R}$. We denote this algebra by $\mathcal{G}_pM$.

A _derivation_ on $\mathcal{G}_pM$ is a linear operator $D \colon \mathcal{G}_pM \to \mathbb{R}$ such that for all $[f], [g] \in \mathcal{G}_pM$,
$$
D[fg] = D[f] \cdot g(p) + f(p) \cdot D[g].
$$
The set of derivations is a subset of the dual space to $\mathcal{G}_pM$ and is closed under addition and scalar multiplication, so it forms a subspace, and we define $T_pM$ to be this $\mathbb{R}$-vector space.

The space of $1$-forms at $P$, denoted $T_p^*M$, is then dual space to $T_pM$. Since $T_pM$ is a subspace of the dual space to $\mathcal{G}_pM$, $T_p^*M$ is a subspace of the double-dual space $\mathcal{G}_p^{**}M$. Since subspaces and quotients are equivalent notions for vector spaces, we can therefore view $T_p^*M$ as a quotient of $\mathcal{G}_p^{**}M$, and via the canonical double-dual isomorphism, as a quotient of $\mathcal{G}_pM$:
$$
\mathcal{G}_pM \overset{\cong}{\longrightarrow} \mathcal{G}_p^{**}M \twoheadrightarrow T_p^*M.
$$
If we can understand the equivalence relation $\sim$ involved in this quotient of $\mathcal{G}_pM$, and in particular specify it without reference to $T_pM$, we have our desired intrinsic construction of the $1$-forms at $p$. That is, $\mathcal{G}_pM / \sim$ is the intrinsically defined space of $1$-forms, and the natural isomorphism to $T_p^*M$ is induced from the double-dual map:

{{< tikz >}}
\begin{tikzcd}
\mathcal{G}_pM \arrow[r, "\cong"] \arrow[d, two heads] & \mathcal{G}_p^{**}M \arrow[d, two heads]\\
\frac{\mathcal{G}_pM}{\sim} \arrow[r, dashed, "\cong"] & T_p^*M
\end{tikzcd}
{{< /tikz >}}

### The Equivalence Relation
Via the double-dual isomorphism, we know that any element of $\mathcal{G}_p^{**}M$ is of the form $[f]^{**} \colon D \mapsto D[f]$ for some $[f] \in \mathcal{G}_pM$. When are two such maps $[f]^{**}$ and $[g]^{**}$ taken to the same equivalence class in $T_p^*M$? Precisely when $D[f] = D[g]$ for all $D \in T_pM$ (note: _not_ necessarily all $D \in \mathcal{G}_p^*M$, unless $[f] = [g]$). Intuitively, this means all partial derivatives for $f$ and $g$ agree at $p$, and therefore $f = g + c$ on a neighborhood of $p$.

More formally, if $\varphi \colon U \to M$ is a chart of $M$, with $U \subseteq \mathbb{R}^n$ and $p \in \varphi(U)$, then $\varphi$ induces a map from partial derivatives at $\varphi^{-1}(p)$ (as operators on differentiable functions on open neighborhoods around $\varphi^{-1}(p)$) to derivations in $T_pM$, given by
$$
\frac{\partial}{\partial\vec{v}} \mapsto \left( [h] \mapsto \frac{\partial}{\partial\vec{v}}(h \circ \varphi) \right).
$$
This means that for any $\vec{v}$, $([h] \mapsto \partial(h \circ \varphi)/\partial\vec{v}) \in T_pM$, so $[f]$ and $[g]$ have the same image under this map; that is,
$$
\frac{\partial}{\partial\vec{v}}(f \circ \varphi) = \frac{\partial}{\partial\vec{v}}(g \circ \varphi).
$$
Since this holds for all $\vec{v}$, we have $f \circ \varphi = (g \circ \varphi) + c$ for some $c \in \mathbb{R}$ on a neighborhood of $\varphi^{-1}(p)$. But then
$$
f \circ \varphi = (g + c) \circ \varphi
$$
on that neighborhood, and since $\varphi$ is bijective, $f = g + c$ on that neighborhood, hence $[f] = [g + c]$.

Thus, if $D[f] = D[g]$ for all $D \in T_pM$, then $[f] = [g + c]$ for some constant $c \in \mathbb{R}$. Conversely, if $[f] = [g + c]$, then for all $D \in T_pM$, we have
$$
D[f] = D[g + c] = D[g] + D[c] = D[g]
$$
since any derivation evaluated on a constant germ is zero:
$$
D[c] = cD[1] = cD[1 \cdot 1] = c(D[1] \cdot 1 + 1 \cdot D[1]) = 2cD[1] = 2D[c] \implies D[c] = 0.
$$
Thus, $[f]$ and $[g]$ are identified under the map
$$
\mathcal{G}_pM \overset{\cong}{\longrightarrow} \mathcal{G}_p^{**}M \twoheadrightarrow T_p^*M
$$
if and only if $[f] = [g + c]$ for some constant $c \in \mathbb{R}$; that is, if and only if $f = g + c$ on some neighborhood of $p$.

## Conclusion
We have shown that if $\sim$ is the equivalence relation
$$
[f] \sim [g] \iff \exists c\bigl[ [f] = [g + c] \bigr],
$$
on $\mathcal{G}_pM$, then the induced map $\mathcal{G}_pM / \sim \to T_p^*M$ from the double-dual map $\mathcal{G}_pM \to \mathcal{G}_p^{**}M$

{{< tikz >}}
\begin{tikzcd}
\mathcal{G}_pM \arrow[r, "\cong"] \arrow[d, two heads] & \mathcal{G}_p^{**}M \arrow[d, two heads]\\
\frac{\mathcal{G}_pM}{\sim} \arrow[r, dashed, "\cong"] & T_p^*M
\end{tikzcd}
{{< /tikz >}}

is an isomorphism because elements of $\mathcal{G}_pM$ are identified under the left hand projection if and only if the corresponding elements of $\mathcal{G}_p^{**}M$ are identified under the right hand projection.

Since $\sim$ is defined without reference to $T_p$M or derivations, this achieves our goal.
