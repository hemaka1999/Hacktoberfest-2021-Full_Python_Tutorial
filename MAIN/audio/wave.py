import wave

with wave.open('audio.wav', "rb") as wav_file:
    # Get basic information.
    n_channels = wav_file.getnchannels()  # Number of channels. (1=Mono, 2=Stereo).
    sample_width = wav_file.getsampwidth()  # Sample width in bytes.
    framerate = wav_file.getframerate()  # Frame rate.
    n_frames = wav_file.getnframes()  # Number of frames.
    comp_type = wav_file.getcomptype()  # Compression type (only supports "NONE").
    comp_name = wav_file.getcompname()  # Compression name.
print(n_channels)
