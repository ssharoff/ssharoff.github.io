<?xml version="1.0" encoding="utf-8" standalone="no"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template name="EXAMPLE_FORMAT">
	<ul>
	    <xsl:for-each select="eg">
		<li>
			<xsl:if test="cit">
				<xsl:value-of select="cit/bibl/date"/> 
				[<xsl:value-of select="cit/bibl/name"/>] 
			</xsl:if>
			<i>
				<xsl:value-of select="q"/>
			</i>
			<xsl:if test="tr">
				--><xsl:value-of select="tr"/>
			</xsl:if>
		</li>
	  </xsl:for-each>
	  </ul>
</xsl:template>

<xsl:template name="SENSE_FORMAT">
    <li><xsl:if test="gramGrp/pos"> (<xsl:value-of select="gramGrp/pos"/>)</xsl:if>
	<xsl:if test="gramGrp/subc">
	<b><i><font face="Arial"><xsl:value-of select="gramGrp/subc"/><br/></font></i></b>
	</xsl:if>
	<b><xsl:value-of select="def"/></b>
	<xsl:if test="usg"> <xsl:for-each select="usg"> <br/><font size="-1"> <xsl:value-of select="@type"/></font>=
	  <u><xsl:value-of select="."/></u>; </xsl:for-each>
	</xsl:if></li>
	<xsl:if test="eg"> <!-- Example(s): --> 
	    <xsl:call-template name="EXAMPLE_FORMAT"/>
	</xsl:if>
	<xsl:if test="xr"> <!-- Cross reference(s): --> Cross reference(s):<ul>
	      <xsl:for-each select="xr">
		<li>
<a href="#{@value}"><font size="-1"> <xsl:value-of select="@type"/></font>=<xsl:value-of select="."/></a>
</li>
	  </xsl:for-each>
	  </ul>
	</xsl:if>

	<xsl:if test="sense"> <!-- Subsenses --> <ol type="a">
		<xsl:for-each select="sense">
			<xsl:call-template name="SENSE_FORMAT"/>
		</xsl:for-each>
	</ol>
	</xsl:if>
      <ul>
      <xsl:for-each select="trans">
	<li><xsl:for-each select="tr"><xsl:value-of select="."/>; </xsl:for-each></li>
	<xsl:if test="gramGrp"><b>Only</b>: <xsl:value-of select="gramGrp"/>; </xsl:if>
	<xsl:if test="usg"> <xsl:for-each select="usg"><font size="-1"><xsl:value-of select="@type"/></font>=
	  <i><xsl:value-of select="."/></i>; </xsl:for-each>
	</xsl:if>
	<xsl:if test="eg"> <!-- Example(s): -->
	    <xsl:call-template name="EXAMPLE_FORMAT"/>
	</xsl:if>
      </xsl:for-each>
      </ul>
  <xsl:if test="re"> 
  	<xsl:for-each select="re">
		Also <b><i><xsl:value-of select="@key"/></i></b>
		<xsl:call-template name="ENTRY_FORMAT"/>
  	</xsl:for-each>
  </xsl:if>
</xsl:template>

<xsl:template name="ENTRY_FORMAT">
  <xsl:if test="gramGrp/pos"> (<xsl:value-of select="gramGrp/pos"/>)</xsl:if>
  <xsl:if test="form/pron"> [<xsl:value-of select="form/pron"/>] </xsl:if>
  <xsl:if test="form/orth"> <xsl:value-of select="form/orth/@type"/>: <i><xsl:value-of select="form/orth"/></i></xsl:if>
  <ol type="1">
  <xsl:for-each select="sense">
	<xsl:call-template name="SENSE_FORMAT"/>
  </xsl:for-each>
  </ol>
  <xsl:if test="eg">
		<xsl:call-template name="EXAMPLE_FORMAT"/>
  </xsl:if>
  <xsl:value-of select="note"/>
  <xsl:value-of select="etym"/>
  <hr/>
</xsl:template>


<xsl:template match="/">
<HTML>
<HEAD>
<title><xsl:value-of select="TEI.2/teiHeader/fileDesc/titleStmt/title"/></title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</HEAD>
<BODY>
<!-- header -->
<h1><xsl:value-of select="TEI.2/teiHeader/fileDesc/titleStmt/title"/></h1>
<author><xsl:value-of select="TEI.2/teiHeader/fileDesc/titleStmt/author"/></author><br/>
         <xsl:value-of select="TEI.2/teiHeader/fileDesc/sourceDesc"/>

<xsl:for-each select="TEI.2/text/body/div">
<h2><xsl:value-of select="head"/></h2>
<b><xsl:value-of select="docAuthor"/></b><br/>
<p><xsl:value-of select="note"/></p>

<xsl:for-each select="entry">
  <xsl:sort select="@key" />
  <a name="{@id}"/><b><xsl:value-of select="@key"/></b> 
  <xsl:call-template name="ENTRY_FORMAT"/>
</xsl:for-each>
</xsl:for-each>
</BODY>
</HTML>
</xsl:template>
</xsl:stylesheet>
