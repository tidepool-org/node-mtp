{
    "targets": [{
        "target_name": "module",
        "sources": [ "./src/module.c" ],
        "conditions": [
            ['OS!="win"',
              {
                "library_dirs": [
                    "../lib"
                ],
                "libraries": [
        	        "-lmtp"
                ],
              }
            ],
            ['OS=="win"',
              {
                  'library_dirs': [
                      '../lib'
                  ],
                  'libraries': [
                    '-l../lib/libmtp.lib'
                  ],
                  'copies': [
                      {
                        'destination': '$(SolutionDir)$(ConfigurationName)',
                        'files': [
                          '<(module_root_dir)/lib/libmtp-9.dll'
                        ]
                      }
                  ]
              }
            ]
        ],
        "include_dirs": [
          "<!(node -e \"require('napi-macros')\")"
        ]
    }],
}
