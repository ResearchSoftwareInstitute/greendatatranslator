from distutils.core import setup 
setup(
      name = 'greentranslator',
      packages = [ 'greentranslator' ], # this must be the same as the name above
      version = '0.8',
      description = 'Green Team BioMedical Data Translator',
      author = 'Steve Cox',
      author_email = 'scox@renci.org',
      include_package_data=True,
      url = 'https://github.com/ResearchSoftwareInstitute/greendatatranslator',
      download_url = 'https://github.com/ResearchSoftwareInstitute/greendatatranslator/archive/0.8.tar.gz',
      keywords = [ 'biomedical', 'environmental', 'exposure', 'clinical' ],
      classifiers = [ ],
    )
