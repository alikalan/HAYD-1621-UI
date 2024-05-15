## Project Overview
This repository contains the frontend code for an emotion detection web application How Are You Doing (hayd-1621). Users can upload or take pictures, which are then analyzed to detect mood based on facial expressions. The moods are categorized into seven types: Angry, Disgusted, Fearful, Happy, Neutral, Sad, Surprised.

## Setup Instructions
1. Clone the repository:

> git clone https://github.com/G-Goose/HAYD-1621-UI.git

2. Install dependencies:

> pip install -r /path/to/requirements.txt

3. Run the application:

> streamlit run main.py

## Pages Description
- **Main UI**: Users can upload or capture a picture to have their mood analyzed and saved.
- **Mood Board**: Displays a historical view of the user's mood uploads.
- **Project Page**: Provides information about the project's goals and objectives.
- **About the Data**: Details about the ResNet50 model, training data, and model performance metrics.

## Technologies Used
- Streamlit
- Google Big Query

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests for any enhancements.
