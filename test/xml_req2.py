def getFlowRule(prio,src1,src,dst,flowid):
	rule = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n<flow xmlns=\"urn:opendaylight:flow:inventory\">\n    <strict>false</strict>\n    <instructions>\n        <instruction>\n            <order>0</order>\n            <apply-actions>\n                <action>\n                    <order>0</order>\n                    <output-action>\n                        <output-node-connector>7</output-node-connector>\n                        <max-length>65535</max-length>\n                    </output-action>\n                </action>\n            </apply-actions>\n        </instruction>\n    </instructions>\n    <table_id>0</table_id>\n    <id>" + str(flowid) + "</id>\n    <cookie_mask>255</cookie_mask>\n	<installHw>true</installHw>\n   <match>\n        <ethernet-match>\n            <ethernet-type>\n                <type>2054</type>\n            </ethernet-type>\n	<ethernet-destination>	<address>3c:07:54:20:a4:91</address>	</ethernet-destination>	<ethernet-source>	<address>00:21:70:da:68:66</address>	</ethernet-source>        </ethernet-match>\n        <ipv4-source>192.168."+ str(src1) + "." + str(src) + "/32</ipv4-source>\n        <ipv4-destination>191.168."+ str(src1)+"." + str(dst) + "/32</ipv4-destination>\n        <in-port>3</in-port>\n    </match>\n    <hard-timeout>10</hard-timeout>\n    <cookie>4</cookie>\n    <idle-timeout>10</idle-timeout>\n    <flow-name>FooXf7</flow-name>\n    <priority>" + str(prio) + "</priority>\n    <barrier>true" \
																																																																																																																																																																																																																																																																																																															 "</barrier>\n</flow>"
	return rule