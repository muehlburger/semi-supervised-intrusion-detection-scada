# A Passive Testing Approach Using a Semi-Supervised Intrusion Detection Model for SCADA Network Traffic

This repository belongs to the paper of the same title by Herbert Mühlburger and Franz Wotawa (IEEE AITest 2022).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23889624.svg)](https://doi.org/10.5281/zenodo.23889624)

## Final pipeline

The folder `final/` holds the pipeline of the paper: PyTorch notebooks, adapted from the [LSTM autoencoder tutorial by Curiousily](https://www.curiousily.com/posts/time-series-anomaly-detection-using-lstm-autoencoder-with-pytorch-in-python/), and the trained models for all six sample sizes.

| File | Content |
| :-- | :-- |
| `final/prepare_data.py` | Builds `final/data/normal.csv` and `final/data/attacks.csv` from the data set |
| `final/train-{250,500,5000}-samples.ipynb` | Training runs with their logs |
| `final/evaluate-20000-samples.ipynb` | Evaluation of the 20,000-sample model, threshold 1.25 |
| `final/evaluate-500-samples.ipynb` | Evaluation of the 500-sample model, threshold 3.6; the sample-size cell shows a later edit, the stored report is the 500-sample run |
| `final/reconstructions-{2000,5000,20000}-samples.ipynb` | Reconstruction plots |
| `final/models/` | Trained models, 150 epochs |

The notebooks expect `data/normal.csv` and `data/attacks.csv` and run from `final/`. They were executed under Python 3.6 and need a pandas version that still has `DataFrame.append`. The stored outputs are kept as they were produced.

Notes on the runs:

- No random seed is set, so each notebook run draws a new sample.
- Training and evaluation run in separate sessions. The evaluation loads a stored model and draws a new split, so its test rows can include rows the model was trained on.
- The evaluation outputs stored here are single runs.
- The thresholds were changed by hand in the report cell. Runs other than the two evaluation notebooks are not stored.
- The training logs for 1,000, 2,000, and 20,000 samples are not stored.

## Preliminary notebooks

`notebooks/` holds two earlier Keras versions. They are not the paper's configuration and do not reproduce the published results. They are published without outputs.

## Data

The data set is not part of this repository. It comes from Egger et al. ([doi:10.1186/s42162-020-00118-4](https://doi.org/10.1186/s42162-020-00118-4)) and is available at <https://github.com/MichaelByteX/Energy-Informatics-2020>. Place `csvDataFeaturesTrain.csv` and `csvDataFeaturesTest.csv` in `data/raw/energy-informatics-2020/`, relative to the repository root.

The data set is highly repetitive: of 288,277 normal packets 5,408 are distinct, of 10,001 attack packets 642.

## Installation

```bash
pip install -r requirements.txt
```

The versions are not pinned. The conda export of the original work is not fully consistent, and current releases may need adjustments.

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
