%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

%define api	0.3

Summary:	Plugins for the Grilo framework
Name:		grilo-plugins
Version:	0.3.8
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://live.gnome.org/Grilo
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(avahi-gobject)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmime-3.0)
BuildRequires:	pkgconfig(gom-1.0)
BuildRequires:	pkgconfig(gupnp-1.0)
BuildRequires:	pkgconfig(gupnp-av-1.0)
BuildRequires:	pkgconfig(libdmapsharing-3.0)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libmediaart-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:	pkgconfig(grilo-0.3)
BuildRequires:	pkgconfig(totem-plparser)
BuildRequires:	pkgconfig(gom-1.0)
Requires:	grilo >= 0.2.6

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Filesystem
- Flickr
- Gravatar
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Podcasts
- Shoutcast
- Tracker
- UPnP
- Vimeo
- Youtube

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-static \
	--disable-shoutcast \
	--disable-bookmarks \
	--enable-filesystem \
	--enable-flickr	\
	--enable-gravatar \
	--enable-jamendo \
	--enable-lastfm-albumart \
	--enable-localmetadata \
	--enable-metadata-store \
	--enable-podcasts \
	--enable-shoutcast \
	--enable-tracker \
	--enable-vimeo \
	--enable-youtube \
	--enable-compile-warnings=no

%make

%install
%makeinstall_std

%find_lang %{name}

# Remove files that will not be packaged
find %{buildroot} -name "*.la" -delete
rm %{buildroot}%{_datadir}/help/C/examples/example-tmdb.c

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_libdir}/grilo-%{api}/libgrl*.so
#{_datadir}/grilo-plugins/
