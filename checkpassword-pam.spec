Summary:	The uniform PAM password-checking interface
Summary(pl):	Jednolity interfejs do sprawdzania hase³ przez PAM
Name:		checkpassword-pam
Version:	0.98
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/sourceforge/checkpasswd-pam/%{name}-%{version}.tar.gz
# Source0-md5:	98e50e7d17f6d5e78d63c3882ec435ca
URL:		http://checkpasswd-pam.sourceforge.net/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
checkpassword provides a simple, uniform password-checking interface
to all root applications. It is suitable for use by applications such
as login, ftpd, and pop3d. checkpassword-pam uses PAM library to check
passwords.

There are checkpassword-compatible tools that support alternate
password databases, secret login names, long passwords, subaccounts,
one-time passwords, detailed accounting, and many other features.
Applications that use the checkpassword interface will work with all
of these tools. Several tools have been specifically designed to
support POP toasters.

%description -l pl
checkpassword udostêpnia prosty, jednolity interfejs do sprawdzania
hase³ we wszystkich aplikacjach z prawami roota. Mo¿e byæ u¿ywany w
aplikacjach takich jak login, ftpd i pop3d. checkpassword-pam u¿ywa
biblioteki PAM do sprawdzania hase³.

Dostêpne s± narzêdzia kompatybilne z checkpassword obs³uguj±ce
alternatywne bazy hase³, ukryte nazwy u¿ytkowników, d³ugie has³a,
podkonta, has³a jednorazowe, szczegó³owy accounting i wiele innych
mo¿liwo¶ci. Aplikacje u¿ywaj±ce interfejsu checkpassword bêd± dzia³aæ
z dowolnym z tych narzêdzi. Kilka narzêdzi zosta³o zaprojektowanych do
obs³ugi POP.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
install checkpassword-pam $RPM_BUILD_ROOT%{_bindir}
install checkpassword-pam.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man8/*
