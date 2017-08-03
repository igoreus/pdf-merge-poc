<?php

class TestPdfMerge
{
    const RETURN_BINARY = 'binary';
    const RETURN_BASE64_STRING = 'base64_string';

    const STREAM_URI = 'pdf-merger-stream';
    const BASE64__URI = 'pdf-merger';

    private $host;
    private $port;

    /**
     * @param string $host
     * @param string $port
     */
    public function __construct($host, $port)
    {
        $this->host = $host;
        $this->port = $port;
    }

    /**
     * @param array $files
     * @param string $returnType
     * @return mixed
     */
    public function merge(array $files, $returnType = self::RETURN_BINARY)
    {
        $curlHandler = curl_init();
        $url = sprintf('%s:%s/%s', $this->host, $this->port,  $returnType == self::RETURN_BINARY ? self::STREAM_URI : self::BASE64__URI);
        $request = [];
        foreach ($files as $file) {
            $request[] = base64_encode(file_get_contents($file));
        }
        $curlOptions = [
            CURLOPT_URL => $url,
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => json_encode($request),
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPAUTH => CURLAUTH_ANY,
            CURLOPT_SSL_VERIFYPEER => false,
            CURLOPT_FOLLOWLOCATION => true,
            CURLOPT_HTTPHEADER => [
                'Content-Type: application/json',
            ],
        ];
        curl_setopt_array($curlHandler, $curlOptions);

        $response = curl_exec($curlHandler);
        curl_close($curlHandler);

        return $response;
    }
}


$merge = new TestPdfMerge('http://192.168.99.1', '8000');

$response = $merge->merge(
    [
        APPLICATION_PATH . "/../data/tmp/2058622149556703075992.pdf",
        APPLICATION_PATH . "/../data/tmp/8058622149556703072967.pdf",
        APPLICATION_PATH . "/../data/tmp/81239574.pdf",
        APPLICATION_PATH . "/../data/tmp/93722745.pdf",
    ]
);

//header("Content-type:application/pdf");
echo $response;
