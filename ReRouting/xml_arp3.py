def getFlowRule(prio,src1,src,dst,flowid):
	rule = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n<flow xmlns=\"urn:opendaylight:flow:inventory\">\n    <strict>false</strict>\n    <instructions>\n        <instruction>\n            <order>0</order>\n            <apply-actions>\n                <action>\n                    <order>0</order>\n                    <output-action>\n                        <output-node-connector>5</output-node-connector>\n                        <max-length>65535</max-length>\n                    </output-action>\n                </action>\n            </apply-actions>\n        </instruction>\n    </instructions>\n    <table_id>0</table_id>\n    <id>10</id>\n    <cookie_mask>255</cookie_mask>\n	<installHw>true</installHw>\n   <match>\n        <ethernet-match>\n            <ethernet-type>\n                <type>2054</type>\n            </ethernet-type>\n	<ethernet-destination>			<address>3c:07:54:20:a4:92</address>			</ethernet-destination>        </ethernet-match>\n		</match>\n    <hard-timeout>60</hard-timeout>\n    <cookie>4</cookie>\n    <idle-timeout>60</idle-timeout>\n    <flow-name>Flow5</flow-name>\n    <priority>2</priority>\n    <barrier>true" \
																																																																																																																																																																																																																																																																																																															 "</barrier>\n</flow>"
	return rule
