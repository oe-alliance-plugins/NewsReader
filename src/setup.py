from setuptools import setup
import setup_translate

pkg = 'Extensions.NewsReader'
setup(name='enigma2-plugin-extensions-newsreader',
       version='1.0',
       description='NewsReader for reading RSS-feeds',
       package_dir={pkg: 'NewsReader'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
