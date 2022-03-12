import java.util.*;

public class Spider {
    
    private static final int MAX_PAGES = 150;

    private Set<String> pagesVisited = new HashSet<String>();

    private List<String> pagesToVisit = new LinkedList<String>();

    private String visitNextURL()
    {
        String url;

        do
        {
            url = this.pagesToVisit.remove(0);
        } while (this.pagesVisited.contains(url));
        this.pagesVisited.add(url);
        return url;
    }

    public void spiderSearch(String baseURL, List<String> searchWords)
    {
        while(this.pagesVisited.length < MAX_PAGES)
        {
            String url;
            Crawl crawler = new Crawl();

            if(this.pagesToVisit.isEmpty()) {
                url = baseURL;
                this.pagesToVisit.add(baseURL);
            }
            else
            {
                url = this.visitNextURL();
            }

            Crawler.crawl(url);

            //look through array of words
            int foundWords = 0;
            for(String word: searchWords) {
                foundWords += crawler.searchForWords(word);
            }
            System.out.println("there were " + foundWords + " words found");

            this.pagesToVisit.addALL(crawler.getLinks());

            System.out.println("done");

        }
    }
}
