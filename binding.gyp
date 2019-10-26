{
  "targets": [
    {
      "target_name": "vad",
      "cflags!": ["-fexceptions"],
      "cflags_cc!": ["-fexceptions", "-std=c++11", "-stdlib=libc++"],
      "sources": [
        "src/webrtcvad.cc",
        "src/vad.cc",
        "src/webrtc/common_audio/signal_processing/complex_bit_reverse.c",
        "src/webrtc/common_audio/signal_processing/complex_fft.c",
        "src/webrtc/common_audio/signal_processing/cross_correlation.c",
        "src/webrtc/common_audio/signal_processing/division_operations.c",
        "src/webrtc/common_audio/signal_processing/downsample_fast.c",
        "src/webrtc/common_audio/signal_processing/energy.c",
        "src/webrtc/common_audio/signal_processing/get_scaling_square.c",
        "src/webrtc/common_audio/signal_processing/min_max_operations.c",
        "src/webrtc/common_audio/signal_processing/resample_48khz.c",
        "src/webrtc/common_audio/signal_processing/resample_by_2_internal.c",
        "src/webrtc/common_audio/signal_processing/resample_fractional.c",
        "src/webrtc/common_audio/signal_processing/spl_init.c",
        "src/webrtc/common_audio/signal_processing/spl_inl.c",
        "src/webrtc/common_audio/signal_processing/spl_sqrt.c",
        "src/webrtc/common_audio/signal_processing/vector_scaling_operations.c",
        "src/webrtc/common_audio/third_party/spl_sqrt_floor/spl_sqrt_floor.c",
        "src/webrtc/common_audio/vad/vad_core.c",
        "src/webrtc/common_audio/vad/vad_filterbank.c",
        "src/webrtc/common_audio/vad/vad_gmm.c",
        "src/webrtc/common_audio/vad/vad_sp.c",
        "src/webrtc/common_audio/vad/webrtc_vad.c",
        "src/webrtc/rtc_base/checks.cc"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "src"
      ],
      "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
      "conditions": [
        [
          'OS=="mac"', {
            "defines": ["WEBRTC_POSIX"]
          }
        ],
        [
          'OS=="win"', {
            "defines": ["WEBRTC_WIN"]
          }
        ],
        [
          'OS=="linux"', {
            "defines": ["WEBRTC_POSIX"]
          }
        ],
      ]
    }
  ]
}
