{
  'targets': [
    { 'target_name': 'platform-osx',
      'product_name': 'mbgl-platform-osx',
      'type': 'static_library',
      'standalone_static_library': 1,
      'hard_dependency': 1,
      'dependencies': [
        'version',
      ],

      'sources': [
        '../platform/default/async_task.cpp',
        '../platform/default/run_loop.cpp',
        '../platform/default/timer.cpp',
        '../platform/darwin/log_nslog.mm',
        '../platform/darwin/string_nsstring.mm',
        '../platform/darwin/application_root.mm',
        '../platform/darwin/asset_root.mm',
        '../platform/darwin/image.mm',
        '../platform/darwin/nsthread.mm',
        '../platform/darwin/reachability.m',
        '../platform/darwin/NSException+MGLAdditions.h',
        '../platform/darwin/NSString+MGLAdditions.h',
        '../platform/darwin/NSString+MGLAdditions.m',
        '../include/mbgl/darwin/MGLTypes.h',
        '../platform/darwin/MGLTypes.m',
        '../include/mbgl/darwin/MGLStyle.h',
        '../platform/darwin/MGLStyle.mm',
        '../include/mbgl/darwin/MGLGeometry.h',
        '../platform/darwin/MGLGeometry_Private.h',
        '../platform/darwin/MGLGeometry.m',
        '../include/mbgl/darwin/MGLAnnotation.h',
        '../include/mbgl/darwin/MGLShape.h',
        '../platform/darwin/MGLShape.m',
        '../include/mbgl/darwin/MGLMultiPoint.h',
        '../platform/darwin/MGLMultiPoint_Private.h',
        '../platform/darwin/MGLMultiPoint.mm',
        '../include/mbgl/darwin/MGLOverlay.h',
        '../include/mbgl/darwin/MGLPointAnnotation.h',
        '../platform/darwin/MGLPointAnnotation.m',
        '../include/mbgl/darwin/MGLPolyline.h',
        '../platform/darwin/MGLPolyline.mm',
        '../include/mbgl/darwin/MGLPolygon.h',
        '../platform/darwin/MGLPolygon.mm',
        '../include/mbgl/osx/Mapbox.h',
        '../include/mbgl/osx/MGLAccountManager.h',
        '../platform/osx/MGLAccountManager_Private.h',
        '../platform/osx/MGLAccountManager.m',
        '../include/mbgl/osx/MGLMapView.h',
        '../platform/osx/MGLMapView_Private.h',
        '../platform/osx/MGLMapView.mm',
        '../include/mbgl/osx/MGLMapView+IBAdditions.h',
        '../platform/osx/MGLMapView+IBAdditions.m',
        '../include/mbgl/osx/MGLMapViewDelegate.h',
        '../platform/osx/MGLOpenGLLayer.h',
        '../platform/osx/MGLOpenGLLayer.mm',
        '../platform/osx/MGLCompassCell.h',
        '../platform/osx/MGLCompassCell.m',
        '../platform/osx/MGLAttributionButton.h',
        '../platform/osx/MGLAttributionButton.m',
        '../include/mbgl/osx/MGLAnnotationImage.h',
        '../platform/osx/MGLAnnotationImage.m',
        '../platform/osx/NSBundle+MGLAdditions.h',
        '../platform/osx/NSBundle+MGLAdditions.m',
        '../platform/osx/NSProcessInfo+MGLAdditions.h',
        '../platform/osx/NSProcessInfo+MGLAdditions.m',
      ],

      'variables': {
        'cflags_cc': [
          '<@(libuv_cflags)',
          '<@(boost_cflags)',
          '<@(variant_cflags)',
        ],
        'libraries': [
          '<@(libuv_static_libs)',
          '$(SDKROOT)/System/Library/Frameworks/Cocoa.framework',
          '$(SDKROOT)/System/Library/Frameworks/CoreLocation.framework',
          '$(SDKROOT)/System/Library/Frameworks/OpenGL.framework',
          '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
          '$(SDKROOT)/System/Library/Frameworks/SystemConfiguration.framework',
        ],
      },

      'include_dirs': [
        '../include/mbgl/osx',
        '../include/mbgl/darwin',
        '../include',
      ],

      'xcode_settings': {
        'OTHER_CPLUSPLUSFLAGS': [ '<@(cflags_cc)' ],
        'CLANG_ENABLE_OBJC_ARC': 'YES',
        'CLANG_ENABLE_MODULES': 'YES',
      },

      'link_settings': {
        'libraries': [ '<@(libraries)' ],
      },

      'direct_dependent_settings': {
        'include_dirs': [
          '../include/mbgl/osx',
          '../include/mbgl/darwin',
          '../include',
        ],
        'mac_bundle_resources': [
          '<!@(find ../platform/osx/resources -type f \! -name \'.*\')',
        ],
      },
    },
  ],
}
