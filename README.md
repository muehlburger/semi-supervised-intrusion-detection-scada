# A Passive Testing Approach Using a Semi-Supervised Intrusion Detection Model for SCADA Network Traffic

This repository belongs to the paper of the same title by Herbert Mühlburger and Franz Wotawa (IEEE AITest 2022).

## Status

The repository holds preliminary notebooks of this study. The final pipeline of the paper could not be recovered.

The notebooks train LSTM autoencoders on the SCADA data set, but they are not the paper's configuration: their epoch counts differ, and the sample-size experiments and the threshold scan are not included. They do not reproduce the published results.

| Notebook | Content |
| :-- | :-- |
| `notebooks/0.6-muehlburger-lstm-autoencoder-multivariate-timeseries.ipynb` | Multivariate LSTM autoencoder, first version |
| `notebooks/0.7-muehlburger-lstm-autoencoder-multivariate-timeseries.ipynb` | Multivariate LSTM autoencoder, later version |

The notebooks are published without outputs.

## Data

The data set is not part of this repository. It comes from Egger et al. and is available at <https://github.com/eggermi/Energy-Informatics-2020>. The notebooks expect `csvDataFeaturesTrain.csv` and `csvDataFeaturesTest.csv` in `data/raw/energy-informatics-2020/`, relative to the repository root.

## Installation

```bash
pip install -r requirements.txt
```

The versions are not pinned, because the original environment is not documented. The notebooks use standalone Keras and may need adjustments for current releases.

## Citation

```bibtex
@inproceedings{muehlburger2022passive,
  title     = {A Passive Testing Approach Using a Semi-Supervised Intrusion Detection Model for {SCADA} Network Traffic},
  author    = {M{\"u}hlburger, Herbert and Wotawa, Franz},
  booktitle = {2022 IEEE International Conference on Artificial Intelligence Testing (AITest)},
  pages     = {42--47},
  year      = {2022},
  doi       = {10.1109/AITest55621.2022.00015}
}
```

## License

[MIT](LICENSE)
