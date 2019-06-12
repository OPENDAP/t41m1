<?xml version="1.0" encoding="UTF-8"?>
<bes:request xmlns:bes="http://xml.opendap.org/ns/bes/1.0#" reqID="[thread:http-nio-8080-exec-5-32]">
  <bes:setContext name="xdap_accept">3.2</bes:setContext>
  <bes:setContext name="dap_explicit_containers">no</bes:setContext>
  <bes:setContext name="errors">xml</bes:setContext>
  <bes:setContext name="max_response_size">0</bes:setContext>
  <bes:setContainer name="catalogContainer" space="catalog">/t41m1/dmrpp_s3/airs/AIRS.2015.01.01.L3.RetStd_IR001.v6.0.11.0.G15013155825.nc.h5.dmrpp</bes:setContainer>
  <bes:define name="d1" space="default">
    <bes:container name="catalogContainer">
      <bes:constraint>ClrOLR_A[0:1:179][0:1:359]</bes:constraint>
    </bes:container>
  </bes:define>
  <bes:get type="dods" definition="d1" />
</bes:request>
