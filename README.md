# webrtcvad

webrtcvad is a cross-platform, native [node.js](https://nodejs.org) [addon](http://nodejs.org/api/addons.html) for detecting speech in raw audio. webrtcvad provides node.js bindings for the native [WebRTC](https://webrtc.org) voice activity detection library.

## Installation

webrtcvad has been tested on Windows 10, macOS 10.14+, and Ubuntu 18.04+ (and may work on other platforms as well).

To install webrtcvad, run:

    yarn add webrtcvad

If you're using this library with Electron, you should probably use [electron-rebuild](https://github.com/electron/electron-rebuild).

## Usage

webrtcvad works with single-channel, 16-bit, signed-integer linear PCM audio sampled at 8kHz, 16kHz, 32kHz, or 48kHz.

You can create a voice activity detector (VAD) with:

    import VAD from "webrtcvad";

    const audio = ...; // Buffer containing exactly 10ms, 20ms, or 30ms of audio data
    const vad = new VAD(16000, 3);
    vad.process(audio);

The `VAD` constructor accepts two arguments. The first is the sample rate (which must be one of the above), and the second is a VAD level, with `0` being the least aggressive (i.e., leading to the most false positives) and `3` being the most aggressive (i.e., leading to the least false positives, but possibly missing actual speech).

The `VAD` object has one method called `process` that returns `true` if the frame contains speech and `false` if not. It takes one argument, a `Buffer` containing exactly 10ms, 20ms, or 30ms of audio. For instance, if you're sampling at 16kHz, then the length of `audio` should be `160`, `320`, or `480`, since the audio must be single-channel, 16-bit.

If you're looking to apply the VAD to live microphone data, take a look at [speech-recorder](https://github.com/serenadeai/speech-recorder), which uses webrtcvad to capture speech from a device's microphone.

## Credits

This module is based on [py-webrtcvad](https://github.com/wiseman/py-webrtcvad).
