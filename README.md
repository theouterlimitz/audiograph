# AudioGraph

This Python script provides a basic audio visualization and analysis tool. It streams audio data from a YouTube URL, generates a 3D plot representing the audio waveform, and calculates the aggregate sum of the audio samples.

## Features

* Fetches audio data from a YouTube video.
* Visualizes the audio waveform in a 3D plot (amplitude over time).
* Calculates the aggregate sum of audio samples.

## Dependencies

* numpy
* matplotlib
* requests
* mpl_toolkits (for 3D plotting)

## Usage

1. Make sure you have the required dependencies installed (`pip install numpy matplotlib requests`).
2. Replace the `url` variable in the script with the YouTube URL of your desired audio source.
3. Run the script: `python audiograph.py` 

## Notes

* The "frequency" axis in the 3D plot is currently just a placeholder. The code doesn't perform any frequency analysis.
* The aggregate sum calculation is a simple example of audio analysis. More sophisticated techniques can be applied for further insights.

## Contributing

Feel free to contribute improvements or additional features! 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
