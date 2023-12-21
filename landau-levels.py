from landau.simulator import LandauLevelSimulator

sim = LandauLevelSimulator(n=18, min_x=-8, max_x=8)
sim.plot_wavefunction()
sim.plot_density(with_classical=True)

sim = LandauLevelSimulator(n=50, min_x=-12, max_x=12)
sim.plot_wavefunction()
sim.plot_density(with_classical=True)

sim = LandauLevelSimulator(n=100, min_x=-15, max_x=15)
sim.plot_wavefunction()
sim.plot_density(with_classical=True)
