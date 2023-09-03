from setuptools import setup
from setuptools import find_packages

setup(
    name='streamlit_stock_project',

    version='0.1.0',

    description='Streamlit project',

    long_description_content_type="text/markdown",

    install_requires=[
        'streamlit',
        'streamlit_lottie',
        'extra_streamlit_components',
        'streamlit_option_menu',
        'trycourier',
        'streamlit_cookies_manager',
    ],

    keywords='streamlit, machine learning, login, sign-up, authentication, cookies',

    packages=find_packages(),

    include_package_data=True,

    python_requires='>=3.9.12',

    classifiers=[

        # 'Intended Audience :: Developers',
        # 'Intended Audience :: ML Engineers',
        # 'Intended Audience :: Streamlit App Developers',

        'License :: OSI Approved :: MIT License',

        'Natural Language :: English',

        'Operating System :: OS Independent',

        # 'Programming Language :: Python :: 3.9.12',

        # 'Topic :: Streamlit',
        # 'Topic :: Authentication',
        # 'Topic :: Login/Sign-Up'

    ]
)