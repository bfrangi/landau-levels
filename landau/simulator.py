class LandauLevelSimulator:
    def __init__(self, n, min_x = None, max_x = None):
        self.n = n
        self.x_number_of_points = 5000 # number of x points
        self.x_arr = None
        self.x_min = min_x
        self.x_max = max_x
        self.xi_arr = None
        self.plt = None

        # Initial wave function
        self.phi_n_min_2 = None
        self.phi_n_min_1 = None

        # Solution
        self.n_landau_level_wf = None
        self.n_landau_level_density = None

        from numpy import sqrt

        # Unit Base
        self.m_e = 9.1093837e-31  # kg = M
        self.hbar_unit = 1.0545718e-34  # J·s = ML²T⁻¹
        self.mtr = 1  # m = L
        self.e = 1.602176634e-19 # C = IT

        # Adimensionalised constants
        self.hbar = 1  # hbar
        self.m = 1.0  # m_e
        self.q = -1.0  # e
        B = 6.6e-16  # T = MT⁻²I⁻¹
        self.B = B/(self.hbar_unit * self.mtr**2)*self.e # hbar e⁻¹ m²

    
    def characteristic_length(self):
        from numpy import sqrt, absolute
        return sqrt(absolute(self.hbar / (self.q * self.B)))
    

    def w_c(self):
        return abs(self.q * self.B / self.m)


    def initial_wavefunction(self):
        from numpy import exp, sqrt, pi
        x_arr = self.x_arr if self.x_arr is not None else self.compute_x_array()
        w = self.w_c()
        self.phi_n_min_2 = ((self.m * w) / (pi * self.hbar))**(1/4) * exp(-(x_arr**2 * self.m * w) / (2 * self.hbar))
        self.phi_n_min_1 = sqrt(2 * pi) * ((self.m * w) / (pi * self.hbar))**(3/4) * x_arr * exp(-(x_arr**2 * self.m * w) / (2 * self.hbar))
    

    def compute_x_array(self):
        from numpy import linspace
        l_char = self.characteristic_length()
        x_max = self.x_max or l_char * 10
        x_min = self.x_min or -l_char * 10
        self.x_arr = linspace(x_min, x_max, self.x_number_of_points)
        return self.x_arr


    def compute_xi_array(self):
        x_arr = self.x_arr if self.x_arr is not None else self.compute_x_array()
        self.xi_arr = (self.m * self.w_c() / self.hbar) * x_arr
        return self.xi_arr
    

    def recurse(self, n = 2):
        if self.phi_n_min_1 is None or self.phi_n_min_2 is None:
            self.initial_wavefunction()
        if self.n == 0:
            return self.phi_n_min_2
        elif self.n == 1:
            return self.phi_n_min_1
        from numpy import sqrt
        xi_arr = self.xi_arr if self.xi_arr is not None else self.compute_xi_array()
        phi_n = sqrt(2 / n) * (
            xi_arr * self.phi_n_min_1 - sqrt((n - 1)/2) * self.phi_n_min_2 
        )
        if n == self.n:
            return phi_n
        self.phi_n_min_2 = self.phi_n_min_1
        self.phi_n_min_1 = phi_n
        return self.recurse(n + 1)


    def compute_wavefunction(self):
        self.n_landau_level_wf = self.recurse()
        return self.n_landau_level_wf

    
    def compute_density(self):
        from numpy import absolute
        self.n_landau_level_wf = self.n_landau_level_wf if self.n_landau_level_wf is not None \
            else self.recurse()
        self.n_landau_level_density = absolute(self.n_landau_level_wf)**2
        return self.n_landau_level_density


    def plot_wavefunction(self):
        self.n_landau_level_wf = self.n_landau_level_wf if self.n_landau_level_wf is not None \
            else self.compute_wavefunction()
        import matplotlib.pyplot as plt
        plt.plot(self.x_arr, self.n_landau_level_wf)
        plt.title(f"Landau Level Wave Function for n = {self.n}")
        plt.xlabel("$x$ ($m$)")
        plt.ylabel("$|\psi(x)|^2$")
        plt.show()
        self.plt = plt
        return self.plt
    

    def plot_density(self, with_classical=False):
        self.n_landau_level_density = self.n_landau_level_density \
            if self.n_landau_level_density is not None else self.compute_density()
        import matplotlib.pyplot as plt
        plt.plot(self.x_arr, self.n_landau_level_density)
        plt.title(f"Landau Level Density Function for n = {self.n}")
        plt.xlabel("$x$ ($m$)")
        plt.ylabel("$|\psi(x)|^2$")
        if with_classical:
            plt.plot(self.x_arr, self.classical_density(self.n))
            plt.legend(["Quantum", "Classical"])
        plt.show()
        self.plt = plt
        return self.plt
    
    
    def classical_density(self, n):
        from numpy import sqrt, pi
        E = self.hbar * self.w_c() * (n + 1/2)
        A = sqrt(2 * E / self.m)
        x_arr = self.x_arr if self.x_arr is not None else self.compute_x_array()
        return (1 / pi) / sqrt(A**2 - x_arr**2)
