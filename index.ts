import bindings from "bindings";
const vadBindings = bindings("vad.node");

export default class VAD {
  private sampleRate: number;
  private instance: any;

  constructor(sampleRate: number = 16000, level: number = 3) {
    this.sampleRate = sampleRate;
    this.instance = new vadBindings.VAD(sampleRate, level);
  }

  private valid(audio: Buffer): boolean {
    return (
      audio.length / 2 == this.sampleRate / 100 ||
      audio.length / 2 == (2 * this.sampleRate) / 100 ||
      audio.length / 2 == (3 * this.sampleRate) / 100
    );
  }

  process(audio: Buffer): boolean {
    if (!this.valid(audio)) {
      throw new Error(
        `Invalid audio length. For a sample rate of ${this.sampleRate}, audio length must be ${(2 *
          this.sampleRate) /
          100}, ${(4 * this.sampleRate) / 100}, or ${(6 * this.sampleRate) / 100}.`
      );
    }

    return this.instance.process(audio, audio.length / 2);
  }
}
