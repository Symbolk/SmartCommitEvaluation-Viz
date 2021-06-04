# SmartCommitEvaluation-Viz

### Requirements
- macOS/Linux
- Python 3.7.0
- PyCharm 2020

### Instructions

1. Open the project in PyCharm, setup the vent as Python 3.7.0, and install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Edit `SmartCommitEvaluation-Viz/config.py` to change the raw data directory:

   ```
   # root dir of raw data
   root_path = str(Path.home()) + '/smartcommit/viz/'
   ```

4. For Controlled Open Source Experiment:

   - Run `rq1/rq1-boxplot-project_method.py` to generate `rq1-baselines.pdf`:  Accuracy of SmartCommit and 3 baseline methods (Figure 7(a) in the paper)
   - Run `rq1/rq1-boxplot-project_length.py` to generate `rq1-length.pdf`:  Accuracy of SmartCommit for different numbers of merged atomic commits (Figure 7(b) in the paper)
   - Run `rq2/rq2-adjustments.py` to generate `reassign_frequency.txt` and `reorder_frequency.txt`: Number of reassign and reorder steps and proportions.

5. For Industrial Field Study:

   - Run `rq3/rq3-scatterplot.py` to generate `rq3.pdf`: the runtime cost with different input sizes;
   - Run `rq4/preprocess.py` first, and other python files then to generate usage distributions (Figure 9 in the paper).