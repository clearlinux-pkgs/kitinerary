#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kitinerary
Version  : 24.05.0
Release  : 123
URL      : https://download.kde.org/stable/release-service/24.05.0/src/kitinerary-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/kitinerary-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/kitinerary-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Data model and extraction system for travel reservation information
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 LGPL-2.0 ODbL-1.0
Requires: kitinerary-data = %{version}-%{release}
Requires: kitinerary-lib = %{version}-%{release}
Requires: kitinerary-license = %{version}-%{release}
Requires: kitinerary-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(poppler)
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kcalendarcore-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : kpkpass-dev
BuildRequires : libxml2-dev
BuildRequires : openssl-dev
BuildRequires : poppler-dev
BuildRequires : qt6base-dev
BuildRequires : zlib-dev
BuildRequires : zxing-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Sources for test files:
pdf417*.png: https://en.wikipedia.org/wiki/PDF417 (CC0)
aztec.png: https://en.wikipedia.org/wiki/Aztec_Code (Public Domain)
uic918-3star.png: https://sourceforge.net/projects/dbuic2vdvbc/ (BSD)

%package data
Summary: data components for the kitinerary package.
Group: Data

%description data
data components for the kitinerary package.


%package dev
Summary: dev components for the kitinerary package.
Group: Development
Requires: kitinerary-lib = %{version}-%{release}
Requires: kitinerary-data = %{version}-%{release}
Provides: kitinerary-devel = %{version}-%{release}
Requires: kitinerary = %{version}-%{release}

%description dev
dev components for the kitinerary package.


%package lib
Summary: lib components for the kitinerary package.
Group: Libraries
Requires: kitinerary-data = %{version}-%{release}
Requires: kitinerary-license = %{version}-%{release}

%description lib
lib components for the kitinerary package.


%package license
Summary: license components for the kitinerary package.
Group: Default

%description license
license components for the kitinerary package.


%package locales
Summary: locales components for the kitinerary package.
Group: Default

%description locales
locales components for the kitinerary package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kitinerary-24.05.0
cd %{_builddir}/kitinerary-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716587419
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716587419
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kitinerary
cp %{_builddir}/kitinerary-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/kitinerary/c011fda7746c087a127999da1c4044854ee42238 || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kitinerary/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kitinerary/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kitinerary/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kitinerary/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kitinerary-%{version}/LICENSES/ODbL-1.0.txt %{buildroot}/usr/share/package-licenses/kitinerary/fb63c741bc85425d4f0fa8b08a5ca2596d416ce9 || :
cp %{_builddir}/kitinerary-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kitinerary/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kitinerary-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kitinerary/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kitinerary-%{version}/src/cli/org.kde.kitinerary-extractor.desktop.license %{buildroot}/usr/share/package-licenses/kitinerary/864bc0eb28c73bd997ac19ff91935ab771846615 || :
cp %{_builddir}/kitinerary-%{version}/src/knowledgedb-generator/timezones.qgs.license %{buildroot}/usr/share/package-licenses/kitinerary/864bc0eb28c73bd997ac19ff91935ab771846615 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kitinerary6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/kf6/kitinerary-extractor
/usr/lib64/libexec/kf6/kitinerary-extractor

%files data
%defattr(-,root,root,-)
/usr/share/mime-packages/application-vnd-kde-itinerary.xml
/usr/share/qlogging-categories6/org_kde_kitinerary.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KItinerary/AbstractExtractor
/usr/include/KPim6/KItinerary/Action
/usr/include/KPim6/KItinerary/AlphaId
/usr/include/KPim6/KItinerary/BERElement
/usr/include/KPim6/KItinerary/BarcodeDecoder
/usr/include/KPim6/KItinerary/BoatTrip
/usr/include/KPim6/KItinerary/Brand
/usr/include/KPim6/KItinerary/BusTrip
/usr/include/KPim6/KItinerary/CalendarHandler
/usr/include/KPim6/KItinerary/CountryDb
/usr/include/KPim6/KItinerary/CreativeWork
/usr/include/KPim6/KItinerary/Datatypes
/usr/include/KPim6/KItinerary/DocumentUtil
/usr/include/KPim6/KItinerary/ELBTicket
/usr/include/KPim6/KItinerary/Event
/usr/include/KPim6/KItinerary/ExtractorCapabilities
/usr/include/KPim6/KItinerary/ExtractorDocumentNode
/usr/include/KPim6/KItinerary/ExtractorDocumentNodeFactory
/usr/include/KPim6/KItinerary/ExtractorDocumentProcessor
/usr/include/KPim6/KItinerary/ExtractorEngine
/usr/include/KPim6/KItinerary/ExtractorFilter
/usr/include/KPim6/KItinerary/ExtractorPostprocessor
/usr/include/KPim6/KItinerary/ExtractorRepository
/usr/include/KPim6/KItinerary/ExtractorResult
/usr/include/KPim6/KItinerary/ExtractorValidator
/usr/include/KPim6/KItinerary/File
/usr/include/KPim6/KItinerary/Flight
/usr/include/KPim6/KItinerary/HtmlDocument
/usr/include/KPim6/KItinerary/HttpResponse
/usr/include/KPim6/KItinerary/IataBcbp
/usr/include/KPim6/KItinerary/IataBcbpSections
/usr/include/KPim6/KItinerary/JsonLdDocument
/usr/include/KPim6/KItinerary/KnowledgeDb
/usr/include/KPim6/KItinerary/LocationUtil
/usr/include/KPim6/KItinerary/MergeUtil
/usr/include/KPim6/KItinerary/Organization
/usr/include/KPim6/KItinerary/PdfDocument
/usr/include/KPim6/KItinerary/PdfImage
/usr/include/KPim6/KItinerary/PdfLink
/usr/include/KPim6/KItinerary/Person
/usr/include/KPim6/KItinerary/Place
/usr/include/KPim6/KItinerary/PriceUtil
/usr/include/KPim6/KItinerary/ProgramMembership
/usr/include/KPim6/KItinerary/Rct2Ticket
/usr/include/KPim6/KItinerary/RentalCar
/usr/include/KPim6/KItinerary/Reservation
/usr/include/KPim6/KItinerary/SSBTicketBase
/usr/include/KPim6/KItinerary/SSBv1Ticket
/usr/include/KPim6/KItinerary/SSBv2Ticket
/usr/include/KPim6/KItinerary/SSBv3Ticket
/usr/include/KPim6/KItinerary/ScriptExtractor
/usr/include/KPim6/KItinerary/SortUtil
/usr/include/KPim6/KItinerary/Taxi
/usr/include/KPim6/KItinerary/Ticket
/usr/include/KPim6/KItinerary/Token
/usr/include/KPim6/KItinerary/TrainTrip
/usr/include/KPim6/KItinerary/Uic9183Block
/usr/include/KPim6/KItinerary/Uic9183Head
/usr/include/KPim6/KItinerary/Uic9183Header
/usr/include/KPim6/KItinerary/Uic9183Parser
/usr/include/KPim6/KItinerary/Uic9183TicketLayout
/usr/include/KPim6/KItinerary/Uic9183Utils
/usr/include/KPim6/KItinerary/VdvBasicTypes
/usr/include/KPim6/KItinerary/VdvTicket
/usr/include/KPim6/KItinerary/VdvTicketContent
/usr/include/KPim6/KItinerary/VdvTicketParser
/usr/include/KPim6/KItinerary/Vendor0080Block
/usr/include/KPim6/KItinerary/Vendor0080VUBlockData
/usr/include/KPim6/KItinerary/Vendor1154Block
/usr/include/KPim6/KItinerary/Visit
/usr/include/KPim6/kitinerary/abstractextractor.h
/usr/include/KPim6/kitinerary/action.h
/usr/include/KPim6/kitinerary/alphaid.h
/usr/include/KPim6/kitinerary/barcodedecoder.h
/usr/include/KPim6/kitinerary/berelement.h
/usr/include/KPim6/kitinerary/boattrip.h
/usr/include/KPim6/kitinerary/brand.h
/usr/include/KPim6/kitinerary/bustrip.h
/usr/include/KPim6/kitinerary/calendarhandler.h
/usr/include/KPim6/kitinerary/countrydb.h
/usr/include/KPim6/kitinerary/creativework.h
/usr/include/KPim6/kitinerary/datatypes.h
/usr/include/KPim6/kitinerary/datatypes_impl.h
/usr/include/KPim6/kitinerary/documentutil.h
/usr/include/KPim6/kitinerary/elbticket.h
/usr/include/KPim6/kitinerary/event.h
/usr/include/KPim6/kitinerary/extractorcapabilities.h
/usr/include/KPim6/kitinerary/extractordocumentnode.h
/usr/include/KPim6/kitinerary/extractordocumentnodefactory.h
/usr/include/KPim6/kitinerary/extractordocumentprocessor.h
/usr/include/KPim6/kitinerary/extractorengine.h
/usr/include/KPim6/kitinerary/extractorfilter.h
/usr/include/KPim6/kitinerary/extractorpostprocessor.h
/usr/include/KPim6/kitinerary/extractorrepository.h
/usr/include/KPim6/kitinerary/extractorresult.h
/usr/include/KPim6/kitinerary/extractorvalidator.h
/usr/include/KPim6/kitinerary/file.h
/usr/include/KPim6/kitinerary/flight.h
/usr/include/KPim6/kitinerary/htmldocument.h
/usr/include/KPim6/kitinerary/httpresponse.h
/usr/include/KPim6/kitinerary/iatabcbp.h
/usr/include/KPim6/kitinerary/iatabcbpsections.h
/usr/include/KPim6/kitinerary/internal/instance_counter.h
/usr/include/KPim6/kitinerary/internal/parameter_type.h
/usr/include/KPim6/kitinerary/internal/strict_equal.h
/usr/include/KPim6/kitinerary/internal/strict_less.h
/usr/include/KPim6/kitinerary/jsonlddocument.h
/usr/include/KPim6/kitinerary/kitinerary_export.h
/usr/include/KPim6/kitinerary/knowledgedb.h
/usr/include/KPim6/kitinerary/locationutil.h
/usr/include/KPim6/kitinerary/mergeutil.h
/usr/include/KPim6/kitinerary/organization.h
/usr/include/KPim6/kitinerary/pdfdocument.h
/usr/include/KPim6/kitinerary/pdfimage.h
/usr/include/KPim6/kitinerary/pdflink.h
/usr/include/KPim6/kitinerary/person.h
/usr/include/KPim6/kitinerary/place.h
/usr/include/KPim6/kitinerary/priceutil.h
/usr/include/KPim6/kitinerary/programmembership.h
/usr/include/KPim6/kitinerary/rct2ticket.h
/usr/include/KPim6/kitinerary/rentalcar.h
/usr/include/KPim6/kitinerary/reservation.h
/usr/include/KPim6/kitinerary/scriptextractor.h
/usr/include/KPim6/kitinerary/sortutil.h
/usr/include/KPim6/kitinerary/ssbticketbase.h
/usr/include/KPim6/kitinerary/ssbv1ticket.h
/usr/include/KPim6/kitinerary/ssbv2ticket.h
/usr/include/KPim6/kitinerary/ssbv3ticket.h
/usr/include/KPim6/kitinerary/taxi.h
/usr/include/KPim6/kitinerary/ticket.h
/usr/include/KPim6/kitinerary/token.h
/usr/include/KPim6/kitinerary/traintrip.h
/usr/include/KPim6/kitinerary/uic9183block.h
/usr/include/KPim6/kitinerary/uic9183head.h
/usr/include/KPim6/kitinerary/uic9183header.h
/usr/include/KPim6/kitinerary/uic9183parser.h
/usr/include/KPim6/kitinerary/uic9183ticketlayout.h
/usr/include/KPim6/kitinerary/uic9183utils.h
/usr/include/KPim6/kitinerary/vdvbasictypes.h
/usr/include/KPim6/kitinerary/vdvticket.h
/usr/include/KPim6/kitinerary/vdvticketcontent.h
/usr/include/KPim6/kitinerary/vdvticketparser.h
/usr/include/KPim6/kitinerary/vendor0080block.h
/usr/include/KPim6/kitinerary/vendor0080vublockdata.h
/usr/include/KPim6/kitinerary/vendor1154block.h
/usr/include/KPim6/kitinerary/visit.h
/usr/include/KPim6/kitinerary_version.h
/usr/lib64/cmake/KPim6Itinerary/KPim6ItineraryConfig.cmake
/usr/lib64/cmake/KPim6Itinerary/KPim6ItineraryConfigVersion.cmake
/usr/lib64/cmake/KPim6Itinerary/KPim6ItineraryTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6Itinerary/KPim6ItineraryTargets.cmake
/usr/lib64/libKPim6Itinerary.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6Itinerary.so.6.1.0
/usr/lib64/libKPim6Itinerary.so.6
/usr/lib64/libKPim6Itinerary.so.6.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kitinerary/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kitinerary/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kitinerary/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kitinerary/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kitinerary/864bc0eb28c73bd997ac19ff91935ab771846615
/usr/share/package-licenses/kitinerary/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kitinerary/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/kitinerary/fb63c741bc85425d4f0fa8b08a5ca2596d416ce9
/usr/share/package-licenses/kitinerary/fca67987925d2ed70e898f6dd9c7fe4b458d416d

%files locales -f kitinerary6.lang
%defattr(-,root,root,-)

