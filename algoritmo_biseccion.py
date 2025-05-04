def f(x):
    print(6*x**4 + 13*x**3 - 4*x**2 - 5*x - 4)
    return 6*x**4 + 13*x**3 - 4*x**2 - 5*x - 4

def bisection(a, b, tol=1e-6, max_iter=1000):
    if f(a) * f(b) >= 0:
        print("El método no puede aplicarse: f(a) y f(b) deben tener signos opuestos.")
        return None

    iter_count = 0
    while (b - a)/2 > tol and iter_count < max_iter:
        m = (a + b) / 2
        fm = f(m)

        if fm == 0 or (b - a)/2 < tol:
            return m  # raíz encontrada

        if f(a) * fm < 0:
            b = m
        else:
            a = m

        iter_count += 1

    return (a + b) / 2  # aproximación de la raíz

# Ejemplo: buscar raíz entre x = -2 y x = -1
raiz = bisection(-3, -2)
if raiz is not None:
    print(f"Raíz encontrada: x ≈ {raiz:.6f}")
