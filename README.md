# F1 Championship Prediction Model 🏎️

## Overview
This machine learning model predicts both Formula 1 World Drivers' Championship (WDC) and World Constructors' Championship (WCC) outcomes using historical F1 data. The model analyzes race results, driver performance, and constructor statistics to generate predictions for upcoming seasons.

## Latest Results (2024 Predictions)

### 🏆 WDC Championship Contenders
1. Max Verstappen (Red Bull) - 57.1%
2. Sergio Perez (Red Bull) - 32.6%
3. Charles Leclerc (Ferrari) - 32.4%
4. Carlos Sainz (Ferrari) - 28.3%
5. Lewis Hamilton (Mercedes) - 19.4%

### 🏢 WCC Championship Contenders
1. Red Bull Racing - 66.9%
2. Ferrari - 32.0%
3. Mercedes - 16.4%
4. Aston Martin - 5.9%
5. Alpine F1 Team - 3.9%

## Model Performance

### WDC Model
- Accuracy: 91.6%
- Precision: 30.0%
- Recall: 85.7%
- F1 Score: 44.4%

### WCC Model
- Accuracy: 89.9%
- Precision: 44.4%
- Recall: 80.0%
- F1 Score: 57.1%

## Features Used

### Driver Features
1. Points (total, average, maximum)
2. Wins
3. Grid positions
4. Race completion rate
5. Recent performance
6. Position consistency

### Constructor Features
1. Points scoring
2. Race wins
3. Grid performance
4. Team reliability
5. Development trend
6. Historical performance

## Technical Details

### Dependencies
```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

### 📁 Project Structure
```bash
f1-ml/
├── data/               # Raw F1 data files
├── preprocessing/      # Data cleaning scripts
├── feature_engineering/# Feature creation
├── modeling/          # ML model implementation
├── utils/             # Helper functions
└── config/            # Configuration files
```

### Installation
```bash
# Clone repository
git clone https://github.com/Modise-Kgosi/f1-ml.git

# Create virtual environment
python -m venv f1-env

# Activate environment
source f1-env/bin/activate  # Unix/macOS
f1-env\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

### Usage
```bash
# Run the prediction pipeline
python main.py
```

## Data Sources
- Formula 1 World Championship (1950-2024)
- Includes race results, qualifying data, and championship standings
- Updated after each race weekend

## Model Features
- Handles both driver and constructor predictions
- Accounts for recent form and historical performance
- Considers team-driver relationships
- Evaluates qualifying and race pace separately
- Tracks development trends throughout seasons

## Future Improvements
- Add weather performance analysis
- Include track-specific performance metrics
- Consider regulation changes impact
- Add driver-team chemistry metrics
- Implement more sophisticated ensemble methods

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Authors
- [Modise](https://github.com/Modise-Kgosi)

## Acknowledgments
- Formula 1 for providing historical data
- The F1 community for insights and feedback
- All contributors to this project
