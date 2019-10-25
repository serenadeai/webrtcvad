#ifndef VAD_H
#define VAD_H

#include <napi.h>

extern "C" {
#include "webrtc/common_audio/vad/include/webrtc_vad.h"
}

class VAD : public Napi::ObjectWrap<VAD> {
 public:
  VAD(const Napi::CallbackInfo& info);
  ~VAD();
  static Napi::Object Init(Napi::Env env, Napi::Object exports);

 private:
  VadInst* instance_;
  int sample_rate_;

  Napi::Value Process(const Napi::CallbackInfo& info);
  static Napi::FunctionReference constructor;
};

#endif
