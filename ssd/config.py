


feat_layers=['block3', 'block4', 'block5', 'block7', 'block8', 'block9', 'block10']
feat_shapes=[(64, 64), (32, 32), (16, 16), (8, 8), (4, 4), (2, 2), (1, 1)]
anchor_size_bounds=[0.10, 0.90]
anchor_sizes=[(20.48, 51.2),
            (51.2, 133.12),
            (133.12, 215.04),
            (215.04, 296.96),
            (296.96, 378.88),
            (378.88, 460.8),
            (460.8, 542.72)]
anchor_ratios=[[2, .5],
               [2, .5, 3, 1./3],
               [2, .5, 3, 1./3],
               [2, .5, 3, 1./3],
               [2, .5, 3, 1./3],
               [2, .5],
               [2, .5]]
anchor_steps=[8, 16, 32, 64, 128, 256, 512],
anchor_offset=0.5,
normalizations=[20, -1, -1, -1, -1, -1, -1],
prior_scaling=[0.1, 0.1, 0.2, 0.2]
num_classes=21