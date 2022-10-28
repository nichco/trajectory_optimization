import numpy as np

raw = np.array(
    [
        [
            2.000000000000000000e00,
            4.500000000000000111e-01,
            1.536799999999999972e-02,
            3.674239999999999728e-01,
            5.592279999999999474e-01,
            -1.258039999999999992e-01,
            -1.248699999999999984e-02,
        ],
        [
            3.500000000000000000e00,
            4.500000000000000111e-01,
            1.985100000000000059e-02,
            4.904470000000000218e-01,
            7.574600000000000222e-01,
            -1.615260000000000029e-01,
            8.987000000000000197e-03,
        ],
        [
            5.000000000000000000e00,
            4.500000000000000111e-01,
            2.571000000000000021e-02,
            6.109189999999999898e-01,
            9.497949999999999449e-01,
            -1.954619999999999969e-01,
            4.090900000000000092e-02,
        ],
        [
            6.500000000000000000e00,
            4.500000000000000111e-01,
            3.304200000000000192e-02,
            7.266120000000000356e-01,
            1.131138999999999895e00,
            -2.255890000000000117e-01,
            8.185399999999999621e-02,
        ],
        [
            8.000000000000000000e00,
            4.500000000000000111e-01,
            4.318999999999999923e-02,
            8.247250000000000414e-01,
            1.271487000000000034e00,
            -2.397040000000000004e-01,
            1.217659999999999992e-01,
        ],
        [
            0.000000000000000000e00,
            5.799999999999999600e-01,
            1.136200000000000057e-02,
            2.048760000000000026e-01,
            2.950280000000000125e-01,
            -7.882100000000000217e-02,
            -2.280099999999999835e-02,
        ],
        [
            1.500000000000000000e00,
            5.799999999999999600e-01,
            1.426000000000000011e-02,
            3.375619999999999732e-01,
            5.114130000000000065e-01,
            -1.189420000000000061e-01,
            -1.588200000000000028e-02,
        ],
        [
            3.000000000000000000e00,
            5.799999999999999600e-01,
            1.866400000000000003e-02,
            4.687450000000000228e-01,
            7.240400000000000169e-01,
            -1.577669999999999906e-01,
            3.099999999999999891e-03,
        ],
        [
            4.500000000000000000e00,
            5.799999999999999600e-01,
            2.461999999999999952e-02,
            5.976639999999999731e-01,
            9.311709999999999710e-01,
            -1.944160000000000055e-01,
            3.357500000000000068e-02,
        ],
        [
            6.000000000000000000e00,
            5.799999999999999600e-01,
            3.280700000000000283e-02,
            7.142249999999999988e-01,
            1.111707999999999918e00,
            -2.205870000000000053e-01,
            7.151699999999999724e-02,
        ],
        [
            0.000000000000000000e00,
            6.800000000000000488e-01,
            1.138800000000000055e-02,
            2.099310000000000065e-01,
            3.032230000000000203e-01,
            -8.187899999999999345e-02,
            -2.172699999999999979e-02,
        ],
        [
            1.500000000000000000e00,
            6.800000000000000488e-01,
            1.458699999999999927e-02,
            3.518569999999999753e-01,
            5.356630000000000003e-01,
            -1.257649999999999879e-01,
            -1.444800000000000077e-02,
        ],
        [
            3.000000000000000000e00,
            6.800000000000000488e-01,
            1.952800000000000022e-02,
            4.924879999999999813e-01,
            7.644769999999999621e-01,
            -1.678040000000000087e-01,
            6.023999999999999841e-03,
        ],
        [
            4.500000000000000000e00,
            6.800000000000000488e-01,
            2.666699999999999973e-02,
            6.270339999999999803e-01,
            9.801630000000000065e-01,
            -2.035240000000000105e-01,
            3.810000000000000192e-02,
        ],
        [
            6.000000000000000000e00,
            6.800000000000000488e-01,
            3.891800000000000120e-02,
            7.172730000000000494e-01,
            1.097855999999999943e00,
            -2.014620000000000022e-01,
            6.640000000000000069e-02,
        ],
        [
            0.000000000000000000e00,
            7.500000000000000000e-01,
            1.150699999999999987e-02,
            2.149069999999999869e-01,
            3.115740000000000176e-01,
            -8.498999999999999611e-02,
            -2.057700000000000154e-02,
        ],
        [
            1.250000000000000000e00,
            7.500000000000000000e-01,
            1.432600000000000019e-02,
            3.415969999999999840e-01,
            5.199390000000000400e-01,
            -1.251009999999999900e-01,
            -1.515400000000000080e-02,
        ],
        [
            2.500000000000000000e00,
            7.500000000000000000e-01,
            1.856000000000000011e-02,
            4.677589999999999804e-01,
            7.262499999999999512e-01,
            -1.635169999999999957e-01,
            3.989999999999999949e-04,
        ],
        [
            3.750000000000000000e00,
            7.500000000000000000e-01,
            2.472399999999999945e-02,
            5.911459999999999493e-01,
            9.254930000000000101e-01,
            -1.966150000000000120e-01,
            2.524900000000000061e-02,
        ],
        [
            5.000000000000000000e00,
            7.500000000000000000e-01,
            3.506800000000000195e-02,
            7.047809999999999908e-01,
            1.097736000000000045e00,
            -2.143069999999999975e-01,
            5.321300000000000335e-02,
        ],
        [
            0.000000000000000000e00,
            8.000000000000000444e-01,
            1.168499999999999921e-02,
            2.196390000000000009e-01,
            3.197160000000000002e-01,
            -8.798200000000000465e-02,
            -1.926999999999999894e-02,
        ],
        [
            1.250000000000000000e00,
            8.000000000000000444e-01,
            1.481599999999999931e-02,
            3.553939999999999877e-01,
            5.435950000000000504e-01,
            -1.317419999999999980e-01,
            -1.345599999999999921e-02,
        ],
        [
            2.500000000000000000e00,
            8.000000000000000444e-01,
            1.968999999999999917e-02,
            4.918299999999999894e-01,
            7.669930000000000359e-01,
            -1.728079999999999894e-01,
            3.756999999999999923e-03,
        ],
        [
            3.750000000000000000e00,
            8.000000000000000444e-01,
            2.785599999999999882e-02,
            6.324319999999999942e-01,
            9.919249999999999456e-01,
            -2.077100000000000057e-01,
            3.159800000000000109e-02,
        ],
        [
            5.000000000000000000e00,
            8.000000000000000444e-01,
            4.394300000000000289e-02,
            7.650689999999999991e-01,
            1.188355999999999968e00,
            -2.332680000000000031e-01,
            5.645000000000000018e-02,
        ],
        [
            0.000000000000000000e00,
            8.299999999999999600e-01,
            1.186100000000000002e-02,
            2.232899999999999885e-01,
            3.261100000000000110e-01,
            -9.028400000000000314e-02,
            -1.806500000000000120e-02,
        ],
        [
            1.000000000000000000e00,
            8.299999999999999600e-01,
            1.444900000000000004e-02,
            3.383419999999999761e-01,
            5.161710000000000464e-01,
            -1.279530000000000112e-01,
            -1.402400000000000001e-02,
        ],
        [
            2.000000000000000000e00,
            8.299999999999999600e-01,
            1.836799999999999891e-02,
            4.554270000000000262e-01,
            7.082190000000000429e-01,
            -1.642339999999999911e-01,
            -1.793000000000000106e-03,
        ],
        [
            3.000000000000000000e00,
            8.299999999999999600e-01,
            2.466899999999999996e-02,
            5.798410000000000508e-01,
            9.088819999999999677e-01,
            -2.004589999999999983e-01,
            1.892900000000000138e-02,
        ],
        [
            4.000000000000000000e00,
            8.299999999999999600e-01,
            3.700400000000000217e-02,
            7.012720000000000065e-01,
            1.097366000000000064e00,
            -2.362420000000000075e-01,
            3.750699999999999867e-02,
        ],
        [
            0.000000000000000000e00,
            8.599999999999999867e-01,
            1.224300000000000041e-02,
            2.278100000000000125e-01,
            3.342720000000000136e-01,
            -9.307600000000000595e-02,
            -1.608400000000000107e-02,
        ],
        [
            1.000000000000000000e00,
            8.599999999999999867e-01,
            1.540700000000000056e-02,
            3.551839999999999997e-01,
            5.433130000000000459e-01,
            -1.364730000000000110e-01,
            -1.162200000000000039e-02,
        ],
        [
            2.000000000000000000e00,
            8.599999999999999867e-01,
            2.122699999999999934e-02,
            4.854620000000000046e-01,
            7.552919999999999634e-01,
            -1.817850000000000021e-01,
            1.070999999999999903e-03,
        ],
        [
            3.000000000000000000e00,
            8.599999999999999867e-01,
            3.178899999999999781e-02,
            6.081849999999999756e-01,
            9.510380000000000500e-01,
            -2.252020000000000133e-01,
            1.540799999999999982e-02,
        ],
        [
            4.000000000000000000e00,
            8.599999999999999867e-01,
            4.744199999999999806e-02,
            6.846989999999999466e-01,
            1.042564000000000046e00,
            -2.333600000000000119e-01,
            2.035400000000000056e-02,
        ],
    ]
)



xt = np.array(raw[:, 0:2])
yt = np.array(raw[:, 2:4])
xlimits = np.array([[-3.0, 10.0], [0.4, 0.90]])

print(np.shape(xt))
print(np.shape(yt))

print(yt)