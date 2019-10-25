#include <napi.h>

#include "vad.h"

Napi::Object InitAll(Napi::Env env, Napi::Object exports) {
  return VAD::Init(env, exports);
}

NODE_API_MODULE(vad, InitAll);
