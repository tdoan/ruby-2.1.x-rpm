%define rubyver         2.2.2
%define rubyabi         2.2

Name:           ruby
Version:        %{rubyver}
Release:        1%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libyaml libyaml-devel libffi libffi-devel
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = %{rubyabi}
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
Obsoletes: ruby < %{rubyabi}
Obsoletes: ruby-libs < %{rubyabi}
Obsoletes: ruby-irb < %{rubyabi}
Obsoletes: ruby-rdoc < %{rubyabi}
Obsoletes: ruby-devel < %{rubyabi}
Obsoletes: rubygems < %{rubyabi}

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*
%{_includedir}/*
%{_datadir}/*
%{_libdir}/*

%changelog
* Web Apr 15 2015 Tony Doan <tdoan@tdoan.com> - 2.2.2
- Update ruby version to 2.2.2
